# Separate PDF release inspection

Checked at 2026-10-12T17:27:53.024289Z by the root AI agent, separate from the PDF builder. No human review is claimed.

I inspected all 19 pages in five rendered contact sheets and four full-size table crops: S010 pages 1–11 and its page-7 table; S013 pages 1–8 and its tables on pages 3, 5 and 6. Text, disclosures, headings, page labels and all table columns are visible. No clipping, overlap, missing glyph or broken table was found. The final short page in each copy follows the source length; neither copy adds blank filler pages.

I read the renderer, text verifier and the two layout records. The verifier compares a second plain-source conversion, each source unit in order, full normalized text, URL annotations, bookmarks and embedded fonts. The saved records report 128 S010 units and 148 S013 units, with no missing or duplicated source text. I did not repeat the author's clean rebuild or all network link checks. A PDF link is not proof that its remote source is currently available.

- S010 PDF SHA-256: `4461a42c1a44cfd0254048b842a59cf9c8f770a2937f7d9fe3bc4550a7d1122e`.
- S013 PDF SHA-256: `912777cbe8fb2743e0fb9a465ccd6dbd54829ccfa9d5d3052f4ea7c3eef5909e`.
- Both use the unchanged manuscripts at commit `40a4eab496feace4373374a43a34a5e5144798d5`.

These are reading copies, not new studies or new source verification. PDF/A, screen-reader accessibility, physical printing and all PDF viewers were not tested. Fonts are embedded subsets from locally available system fonts; no standalone font file is redistributed. The existing manuscript evidence limits remain in force.

The first whitespace check treated a PDF as text and reported its internal PDF spaces. The release adds `*.pdf binary` in `.gitattributes`, preserving the exact PDF bytes and disabling text conversion for PDF files. The subsequent staged whitespace check passed.
