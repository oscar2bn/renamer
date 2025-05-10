from pathlib import Path as p

for idx, f in enumerate(p("~/testpics").expanduser().iterdir(), 1):
    print(idx, f.name)
