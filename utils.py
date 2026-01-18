from pathlib import Path
from sys import exit
from os import listdir
import time
import csv



def parse_csv(path: Path) -> list:
    """
    Read one day's menu (one dining hall)
    :param path: file path
    :return:
    """
    ret = []
    try:
        print(f"========PARSING {str(path)}========")
        with path.open("r",encoding="utf-8") as filehandle:
            reader = csv.reader(filehandle)
            for row in reader:
                final = [ele for ele in row if not ele == ""]
                if len(final) == 0: ret.append([])
                else: ret.append(final)
                print(final)
        print(f"========PARSING {str(path)} SUCCESS========")
        return ret
    except Exception as exc:
        print("Exception")
        print(str(exc))
        exit(1)


def parse_dining(path: Path) -> list:
    print(f"########PARSING DINING {str(path)}########")
    try:
        dirs = listdir(path)
        dirs.sort()
        ret = []
        curIndex = 1
        for folderdir in dirs:
            while int(folderdir) > curIndex:
                ret.append([])
                curIndex+=1
            filedir = path / folderdir / "details.csv"
            ret.append(parse_csv(filedir))
            curIndex += 1
        print(f"########PARSING  DINING{str(path)} SUCCESS########")
        return ret
    except Exception as exc:
        print("Exception")
        print(str(exc))
        exit(1)

def getFutureTime(curtime: str,days: int) -> list:
    ret = []
    try:
        print(f"########PARSING TIME########")
        firstTime = time.mktime(time.strptime(curtime,"%Y-%m-%d"))
        ret.append(time.strftime("%Y-%m-%d", time.localtime(firstTime)))
        for i in range(days):
            firstTime += 86400
            ret.append(time.strftime("%Y-%m-%d",time.localtime(firstTime)))
        print(f"########PARSING TIME SUCCESS########")
        return ret
    except Exception as exc:
        print("Exception")
        print(str(exc))
        exit(1)