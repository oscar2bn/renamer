### Utilisation

```bash
# Simulation
python renamer.py ~/testpics --prefix IMG_ --ext .jpg --dry-run

# Renommage réel sans écraser
python renamer.py ~/testpics --prefix IMG_ --ext .jpg

# Renommage réel en écrasant les collisions
python renamer.py ~/testpics --prefix IMG_ --ext .jpg --force

