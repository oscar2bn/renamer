from pathlib import Path
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("src")
parser.add_argument("--dest", required=True)           # booléen
parser.add_argument("--dry-run", action="store_true")
parser.add_argument("--overwrite", action="store_true")
args = parser.parse_args()

dest = Path(args.dest).expanduser()
src  = Path(args.src).expanduser()

if not src.is_file():
    raise SystemExit(f"{src} n'est pas un fichier")

if dest.exists() and not args.overwrite:
    raise SystemExit(f"{dest} existe déjà, ajoutez --overwrite pour l'écraser")

print(f"{src}  →  {dest}", "[simulation]" if args.dry_run else "")

if not args.dry_run:
    shutil.copy2(src, dest)

