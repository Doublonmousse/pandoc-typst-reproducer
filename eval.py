## small helper file to run pandoc on all files, and store log information or errors if needed
# %%
import os
from pathlib import Path

current = Path.cwd()
typ_files = list(current.glob("**/*.typ"))

for file in typ_files:
    name = file.with_suffix("").name
    rel_path = file.relative_to(current)
    output_tex = file.with_suffix(".tex").relative_to(current)
    log_file = (file.parent / f"{name}_log.txt").relative_to(current)

    print(rel_path)
    print(output_tex)

    ## eval pandoc and > into a log file
    out = os.system(f"pandoc {rel_path} -o {output_tex} &> {log_file}")
