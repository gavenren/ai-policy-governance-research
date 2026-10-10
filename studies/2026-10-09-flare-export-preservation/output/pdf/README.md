# PDF artifact and build record

`paper.pdf` is the six-page rendering of this study's `paper.md`.
`render-manifest.json` records the source, renderer, font and PDF hashes, exact
dependency versions, render command, timestamps and artifact QA scope.

Run from the research repository root. Create the free local dependency environment
once, then render with the pinned packages (the recorded build used Python 3.13.7):

```sh
python3 -m venv .local-tools/pdf-render
.local-tools/pdf-render/bin/python -m pip install -r scripts/requirements-pdf.txt
.local-tools/pdf-render/bin/python scripts/render_paper.py studies/2026-10-09-flare-export-preservation/paper.md studies/2026-10-09-flare-export-preservation/output/pdf/paper.pdf --link-base https://github.com/gavenren/ai-policy-governance-research/blob/main/studies/2026-10-09-flare-export-preservation/paper.md
```

Final checks on 2026-10-10 UTC confirmed a byte-identical rerender, complete body
text extraction after Markdown and layout normalization, and 22 link annotations
resolving to 19 distinct expected HTTPS destinations. Link target encoding was
checked locally; remote availability was not rechecked during this artifact QA.
All six pages were rendered and visually inspected by a Codex AI agent. No
clipping, overlap, broken glyphs or table layout issues were found. This is an
artifact fidelity check, not human review or scientific validation.
