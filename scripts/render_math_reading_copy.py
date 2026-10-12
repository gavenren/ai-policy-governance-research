#!/usr/bin/env python3
"""Reading PDFs for the exact Markdown subset in S014 and S015.

ReportLab lays out prose. Matplotlib mathtext supplies exact vector glyph
positions and rules. Unsupported syntax raises; LaTeX commands are not replaced.
Equation tags are explicit, separately typeset labels. No network or TeX used.
"""
from __future__ import annotations
import argparse,base64,hashlib,json,re
from dataclasses import dataclass
from datetime import datetime,timezone
from html import escape
from pathlib import Path
from urllib.parse import urljoin
import matplotlib
matplotlib.use('Agg')
from matplotlib.mathtext import MathTextParser
from matplotlib.font_manager import FontProperties
import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph,SimpleDocTemplate,Flowable,Table,TableStyle,Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from io import BytesIO
from render_reading_copy import TOKEN,LINK,plain

INLINE_MATH=re.compile(r'(?<!\$)\$(?![\s$])([^$\n]*?\S)\$(?![\w$])')
DISPLAY=re.compile(r'\$\$(.*?)\$\$',re.S)
# A transparent parse placeholder is replaced by a MathImage before layout.
PIXEL=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFgAI/ScLbtAAAAABJRU5ErkJggg==')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()

@dataclass
class Block:
    kind:str
    text:str=''
    level:int=0
    rows:list|None=None

def parse(text):
    blocks=[];pending=[];rows=[];math=[];inside=False
    def prose():
        if pending:blocks.append(Block('paragraph',' '.join(pending)));pending.clear()
    def table():
        if rows:
            assert len({len(r) for r in rows})==1
            blocks.append(Block('table',rows=list(rows)));rows.clear()
    for line in text.splitlines()+['']:
        if line.strip()=='$$':
            prose();table()
            if inside:blocks.append(Block('math','\n'+'\n'.join(math)+'\n'));math=[]
            inside=not inside;continue
        if inside:math.append(line);continue
        if line.startswith('|'):
            prose();cells=[x.strip() for x in line.strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?',x.replace(' ','')) for x in cells):rows.append(cells)
            continue
        table()
        if not line.strip():prose()
        elif (m:=re.match(r'^(#{1,3}) (.*)$',line)):
            prose();blocks.append(Block('heading',m[2],len(m[1])))
        elif line.startswith('- '):prose();blocks.append(Block('bullet',line[2:]))
        else:
            assert not re.match(r'^(#{4,}|```|~~~|<|\\|\$\$)',line),line
            pending.append(line)
    assert not inside,'Unclosed display math'
    return blocks

class MathImage:
    def __init__(self,entry):self.entry=entry

class Registry:
    def __init__(self):
        matplotlib.rcParams.update({'mathtext.fontset':'stix','mathtext.default':'it','font.family':'STIXGeneral'})
        self.parser=MathTextParser('path');self.entries=[];self.fonts={}
    def add(self,raw,display,size):
        tag=None;expression=raw.strip()
        if '\\tag' in expression:
            m=re.search(r'\s*\\tag\{([0-9]+)\}\s*$',expression);assert display and m,'Unsupported tag'
            tag=m[1];expression=expression[:m.start()]
        assert '\\tag' not in expression
        # Whitespace between display lines is TeX whitespace, not an equation break.
        parsed=self.parser.parse('$'+expression.replace('\n',' ')+'$',dpi=72,prop=FontProperties(family='STIXGeneral',size=size))
        glyphs=[]
        for font,fontsize,codepoint,x,y in parsed.glyphs:
            path=Path(font.fname);digest=sha(path);name='Math'+digest[:16]
            if name not in self.fonts:
                pdfmetrics.registerFont(TTFont(name,str(path)));self.fonts[name]={'file':path.name,'sha256':digest}
            # A required Unicode glyph must exist; no silent font fallback here.
            assert int(codepoint) in pdfmetrics.getFont(name).face.charToGlyph,(path,codepoint)
            glyphs.append({'font':name,'size':float(fontsize),'codepoint':int(codepoint),'x':float(x),'y':float(y)})
        e={'id':f'Math{len(self.entries):03d}','raw_latex':raw,'source_latex_sha256':hashlib.sha256(raw.encode()).hexdigest(),
           'display':display,'tag':tag,'width':float(parsed.width),'height':float(parsed.height),'depth':float(parsed.depth),
           'glyphs':glyphs,'rules':[[float(x) for x in rule] for rule in parsed.rects],'placements':[]}
        assert e['width']>0 and e['height']>0
        self.entries.append(e);return e

class MathCanvas(Canvas):
    registry:Registry
    def math_form(self,e):
        if not self.hasForm(e['id']):
            self.beginForm(e['id'],0,0,e['width'],e['height'])
            self.setFillColor(colors.HexColor('#15212A'))
            for g in e['glyphs']:
                self.setFont(g['font'],g['size']);self.drawString(g['x'],g['y']+e['depth'],chr(g['codepoint']))
            for x,y,w,h in e['rules']:self.rect(x,y+e['depth'],w,h,stroke=0,fill=1)
            self.endForm()
    def draw_math(self,e,x,y):
        self.math_form(e);ax,ay=self.absolutePosition(x,y)
        e['placements'].append({'page':self.getPageNumber(),'x':ax,'y':ay,'width':e['width'],'height':e['height']})
        self.saveState();self.translate(x,y);self.doForm(e['id']);self.restoreState()
    def drawImage(self,image,x,y,width=None,height=None,*args,**kwargs):
        if isinstance(image,MathImage):
            e=image.entry;assert abs(width-e['width'])<1e-5 and abs(height-e['height'])<1e-5
            self.draw_math(e,x,y);return e['width'],e['height']
        return super().drawImage(image,x,y,width,height,*args,**kwargs)

class Equation(Flowable):
    def __init__(self,e,width):
        super().__init__();self.e=e;self.width=width;self.height=e['height']+16
        assert e['width']<width-40,'Display equation does not fit at full font size'
    def draw(self):
        e=self.e;self.canv.draw_math(e,(self.width-e['width'])/2,8)
        if e['tag']:
            self.canv.setFont('ReadingRegular',11);self.canv.drawRightString(self.width,8+e['depth'],'('+e['tag']+')')

class Doc(SimpleDocTemplate):
    def afterFlowable(self,f):
        if hasattr(f,'outline'):
            title,key,level=f.outline;self.canv.bookmarkPage(key);self.canv.addOutlineEntry(title,key,level,False)

def inline(text,link_base,registry,size):
    # Protect true math before applying Markdown emphasis/link formatting.
    equations=[]
    def math(m):
        e=registry.add(m[1],False,size);equations.append(e);return '\x01'+e['id']+'\x02'
    text=INLINE_MATH.sub(math,text)
    def styled(s):
        out=[]
        for part in TOKEN.split(s):
            if (m:=LINK.match(part)):out.append('<link color="#185B77" href="'+escape(urljoin(link_base,m[2]),quote=True)+'">'+styled(m[1])+'</link>')
            elif part.startswith('**') and part.endswith('**'):out.append('<b>'+styled(part[2:-2])+'</b>')
            elif part.startswith('*') and part.endswith('*'):out.append('<i>'+styled(part[1:-1])+'</i>')
            elif part.startswith('`') and part.endswith('`'):out.append(escape(part[1:-1]))
            else:out.append(escape(part))
        return ''.join(out)
    s=styled(text)
    for e in equations:
        # ImageReader accepts a data URI; it is used only to parse the spacer.
        uri='data:image/png;base64,'+base64.b64encode(PIXEL).decode()
        tag=f'<img src="{uri}" width="{e["width"]}" height="{e["height"]}" valign="{-e["depth"]}"/>'
        s=s.replace('\x01'+e['id']+'\x02',tag)
    return s,equations

def paragraph(text,style,link_base,registry,bullet=False):
    markup,eq=inline(text,link_base,registry,style.fontSize)
    # A deep summation subscript needs room below its own line, not just above
    # the next line. Fixed paragraph leading avoids ReportLab image descent overlap.
    if eq:
        needed=max(style.leading,max(e['height'] for e in eq)+3)
        style=ParagraphStyle(style.name+'Math',parent=style,leading=needed,autoLeading='off')
    p=Paragraph(markup,style,bulletText='•' if bullet else None)
    found=[f for f in p.frags if hasattr(f,'cbDefn') and f.cbDefn.kind=='img']
    assert len(found)==len(eq)
    for f,e in zip(found,eq):f.cbDefn.image=MathImage(e)
    return p

def build(source,destination,study,commit,fonts):
    reportlab.rl_config.invariant=True;registry=Registry();blocks=parse(source.read_text())
    source=source.resolve();destination=destination.resolve()
    raw=source.read_text();link_base=f'https://github.com/gavenren/ai-policy-governance-research/blob/{commit}/'+str(source.relative_to(Path.cwd()))
    for key,path in fonts.items():pdfmetrics.registerFont(TTFont('Reading'+key,str(path)))
    pdfmetrics.registerFontFamily('ReadingRegular',normal='ReadingRegular',bold='ReadingBold',italic='ReadingItalic',boldItalic='ReadingBoldItalic')
    body=ParagraphStyle('Body',fontName='ReadingRegular',fontSize=11,leading=14.5,autoLeading='max',spaceAfter=7.2,allowWidows=False,allowOrphans=False,splitLongWords=False,textColor=colors.HexColor('#15212A'))
    title=ParagraphStyle('Title',parent=body,fontName='ReadingBold',fontSize=22,leading=26,spaceAfter=8,keepWithNext=True)
    subtitle=ParagraphStyle('Subtitle',parent=body,fontSize=13,leading=17,spaceAfter=12,keepWithNext=True,textColor=colors.HexColor('#455660'))
    heading=ParagraphStyle('Heading',parent=body,fontName='ReadingBold',fontSize=13,leading=16,spaceBefore=12,spaceAfter=7,keepWithNext=True)
    small=ParagraphStyle('Disclosure',parent=body,fontSize=9.2,leading=12,spaceAfter=6,textColor=colors.HexColor('#455660'))
    cell=ParagraphStyle('Cell',parent=body,fontSize=9.5,leading=12.1,spaceAfter=0)
    cellhead=ParagraphStyle('CellHead',parent=cell,fontName='ReadingBold')
    bullet=ParagraphStyle('Bullet',parent=body,leftIndent=11,firstLineIndent=0,bulletIndent=0,bulletFontName='ReadingRegular',bulletFontSize=11)
    width=499.68;story=[]
    for i,b in enumerate(blocks):
        if b.kind=='heading':
            issub=i==1 and b.level==2
            p=paragraph(b.text,title if b.level==1 else subtitle if issub else heading,link_base,registry)
            if not issub:p.outline=(plain(b.text),f'heading-{i}',b.level-1)
            story.append(p)
            if issub:story.append(Paragraph(f'PDF reading copy · <link color="#185B77" href="{link_base}">Versioned manuscript source</link> · {study}',small))
        elif b.kind=='math':story.append(Equation(registry.add(b.text,True,12),width))
        elif b.kind in ['paragraph','bullet']:
            style=bullet if b.kind=='bullet' else small if (i<8 and b.text.startswith('**')) else body
            p=paragraph(b.text,style,link_base,registry,b.kind=='bullet')
            if i+1<len(blocks) and blocks[i+1].kind=='math':p.keepWithNext=True
            story.append(p)
        elif b.kind=='table':
            n=len(b.rows[0]);ratios=[.32,.13,.19,.16,.20] if 'Participating' in b.rows[0][0] else [.34,.10,.16,.20,.20]
            assert n==5
            table=Table([[paragraph(c,cellhead if j==0 else cell,link_base,registry) for c in row] for j,row in enumerate(b.rows)],colWidths=[width*x for x in ratios],repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EAF0F3')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.7,colors.HexColor('#607A89')),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#D4DEE4')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
            story.extend([table,Spacer(1,8)])
    # Formula coverage is independently checked against the source inventory.
    display_raw=[m[1] for m in DISPLAY.finditer(raw)]
    inline_raw=[m[1] for m in INLINE_MATH.finditer(DISPLAY.sub('',raw))]
    assert [e['raw_latex'] for e in registry.entries if e['display']]==display_raw
    assert [e['raw_latex'] for e in registry.entries if not e['display']]==inline_raw
    destination.parent.mkdir(parents=True,exist_ok=True)
    doc=Doc(str(destination),pagesize=(612,792),leftMargin=56.16,rightMargin=56.16,topMargin=50.4,bottomMargin=48.96,
            title=plain(blocks[0].text),author='AI-assisted complete-study draft; no human peer review',subject=f'{study}; manuscript SHA-256 {sha(source)}',creator='ReportLab and mathtext vector reading-copy builder',pageCompression=1)
    def furniture(c,d):
        c.saveState();c.setFillColor(colors.HexColor('#52616A'));c.setFont('ReadingRegular',8)
        if d.page>1:
            c.drawString(56.16,764.64,study+' | '+plain(blocks[0].text));c.setStrokeColor(colors.HexColor('#CDD8DD'));c.setLineWidth(.35);c.line(56.16,759.6,555.84,759.6)
        c.drawString(56.16,24.48,'AI-assisted complete-study draft | No human peer review');c.drawRightString(555.84,24.48,str(d.page));c.restoreState()
    doc.build(story,onFirstPage=furniture,onLaterPages=furniture,canvasmaker=MathCanvas)
    assert all(len(e['placements'])==1 for e in registry.entries),'Lost or duplicated equation'
    record={'built_utc':utc(),'source_sha256':sha(source),'source_commit':commit,'source_url':link_base,'pdf_sha256':sha(destination),
            'builder_sha256':sha(__file__),'reportlab':reportlab.Version,'matplotlib':matplotlib.__version__,'study':study,
            'math_fonts':registry.fonts,'prose_fonts':{k:{'file':p.name,'sha256':sha(p)} for k,p in fonts.items()},
            'equations':registry.entries,'inline_math_count':len(inline_raw),'display_math_count':len(display_raw),
            'literal_dollar_count':INLINE_MATH.sub('',DISPLAY.sub('',raw)).count('$'),
            'transformation':'No math command substitution. Strip math delimiters; TeX whitespace across display lines becomes a space. Four LaTeX tag commands in S015 are parsed and drawn as separate visible equation numbers. All source formula bytes are retained in this ledger.'}
    (destination.parent/'math-layout.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k not in ['equations','math_fonts','prose_fonts']},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('destination',type=Path);p.add_argument('--study-id',required=True);p.add_argument('--source-commit',required=True)
    p.add_argument('--font-directory',type=Path,default=Path('/System/Library/Fonts/Supplemental'))
    a=p.parse_args();fonts={k:a.font_directory/v for k,v in {'Regular':'Times New Roman.ttf','Bold':'Times New Roman Bold.ttf','Italic':'Times New Roman Italic.ttf','BoldItalic':'Times New Roman Bold Italic.ttf'}.items()}
    build(a.source,a.destination,a.study_id,a.source_commit,fonts)
