#!/usr/bin/env python3
import argparse
from pathlib import Path

def parse_args():
    p = argparse.ArgumentParser(description="Renomme des fichiers en lot")
    p.add_argument("folder", help="Dossier cible")
    p.add_argument("--prefix", default="", help="Préfixe ajouté")
    p.add_argument("--ext",    default="", help="Filtre (.jpg)")
    p.add_argument("--dry-run", action="store_true",
                   help="Affiche sans renommer")
    p.add_argument("--force",  action="store_true",
                   help="Écrase les fichiers cibles s'ils existent")
    return p.parse_args()

def main():
    args = parse_args()
    base = Path(args.folder).expanduser()

    if not base.is_dir():
        raise SystemExit(f"{base} n'est pas un dossier")

    files = sorted(f for f in base.iterdir()
                   if f.is_file() and (args.ext == "" or f.suffix == args.ext))

    if not files:
        print("Aucun fichier correspondant.")
        return

    taken = {f.name for f in base.iterdir() if f.is_file()}  # noms déjà présents

    for idx, f in enumerate(files, 1):
        i = idx
        while True:
            new_name = f"{args.prefix}{i:04d}{f.suffix}"
            target   = f.with_name(new_name)

            if (target.name in taken) and not args.force:
                i += 1              # collision → numéro suivant
                continue
            break

        taken.add(target.name)      # réserve même en dry-run

        if args.dry_run:
            print(f"{f.name} -> {target.name}")
        else:
            if target.exists() and args.force:
                print(f"⚠️  {target.name} sera écrasé")
            f.rename(target)

if __name__ == "__main__":
    main()

