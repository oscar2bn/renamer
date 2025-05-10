from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("folder")
parser.add_argument("--ext", default=".jpg")
args = parser.parse_args()

base = Path(args.folder).expanduser()

if not base.is_dir():
    raise SystemExit(f"{base} n'est pas un dossier")

count = sum(1 for f in base.iterdir()
            if f.is_file() and f.suffix.lower() == args.ext.lower())

print(f"{count} fichier(s) {args.ext} dans {base}")


