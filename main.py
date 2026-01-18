from pathlib import Path
from sys import exit
from utils import *
from json import dump

_DATA_DIR = Path.cwd() / "data"
NORTH = _DATA_DIR / "north"
SOUTH = _DATA_DIR / "south"
DATE = _DATA_DIR / "date"
OUTPUTDIR = Path.cwd() / "output" / "data.json"

STARTUP = """\
EatInNK Parser
Copyright 2025-2026 APG
"""


gen_tree = {
    "days":[],
    "detail":{
        "north":[],
        "south":[]
    }
}


if __name__ == "__main__":
    if (not DATE.is_file()) or (not NORTH.is_dir()) or (not SOUTH.is_dir()):
        print("DATA FILE NOT AVAILABLE")
        exit(1)
    print(STARTUP)
    southdata = parse_dining(SOUTH)
    northdata = parse_dining(NORTH)
    days = max(len(southdata),len(northdata))
    gen_tree["detail"]["south"] = parse_dining(SOUTH)
    gen_tree["detail"]["north"] = parse_dining(NORTH)
    with DATE.open("r",encoding="utf-8") as filehandle:
        BeginTime  = filehandle.read()
    gen_tree["days"] = getFutureTime(BeginTime,days)
    with OUTPUTDIR.open("w",encoding="utf-8") as filehandle:
        dump(gen_tree,filehandle,ensure_ascii=False)

