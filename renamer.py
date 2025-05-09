#!/usr/bin/env python3
import argparse
from pathlib import Path

def parse_args():
    p = argparse.ArgumentParser(description="Renomme des fichiers en lot")
    p.add_argument("folder", help="Dossier cible")
    p.add_argument("--prefix", default="", help="Préfixe ajouté")
    p.add_argument("--ext", default="", help="Filtre par extension (.jpg)")
    p.add_argument("--dry-run", action="store_true",
                   help="Affiche sans renommer")
    return p.parse_args()

def main():
    args = parse_args()
    base = Path(args.folder).expanduser()
    if not base.is_dir():
        raise SystemExit(f"{base} n'est pas un dossier")

    files = sorted(f for f in base.iterdir()
                   if f.is_file() and (args.ext == "" or f.suffix == args.ext))

    for idx, f in enumerate(files, 1):
        new_name = f"{args.prefix}{idx:04d}{f.suffix}"
        target   = f.with_name(new_name)
        if args.dry_run:
            print(f"{f.name} -> {target.name}")
        else:
            f.rename(target)

if __name__ == "__main__":
    main()
