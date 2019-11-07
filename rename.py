from glob import glob
from os import rename
import datetime
import os

fnames = glob("./phd*.org")

for fn in fnames:
    i = fn.rsplit('/', 1)[-1]
    i = i.split('-')
    y = i[2]
    w = i[3][0:2]
    d = f"{y}-W{w}"
    r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
    m = r.month
    direc = f"./phd-diaries/{y}/{m}"
    if not os.path.exists(direc):
        os.makedirs(direc)
    rename(fn, f"./phd-diaries/{y}/{m}/{w}.org")
