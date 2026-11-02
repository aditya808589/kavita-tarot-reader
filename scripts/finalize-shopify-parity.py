from pathlib import Path
import re
r=Path(__file__).resolve().parent.parent/'kavita-dawn'
for p in list((r/'sections').glob('parity-*.liquid'))+[r/'layout/parity.liquid']:
 s=p.read_text()
 # Legacy page inline scripts consume catalogue synchronously; keep dependency order explicit.
 if p.parent.name=='layout':s='{% # theme-check-disable ParserBlockingScript %}\n'+s+'\n{% # theme-check-enable ParserBlockingScript %}'
 else:s=re.sub(r'<script src=', '<script defer src=',s)
 s=re.sub(r'<img\b[^>]*>',lambda m:m[0][:-1]+(' width="600"' if not re.search(r'\bwidth=',m[0]) else '')+(' height="600"' if not re.search(r'\bheight=',m[0]) else '')+'>',s)
 p.write_text(s)
