#!/usr/bin/env python3

import pandas
from collections import defaultdict

day = 7
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 7 Init

    Create a DataFrame from a text file.
    """
    inlist = defaultdict(int)
    curdir = []
    with open(infile, 'r') as f:
        for line in f.read().split('\n'):
            thisline = line.split(' ')
            if thisline[0] == '$':
                if thisline[1] == 'cd':
                    if thisline[2] == '/':
                        curdir = ['/']
                    elif thisline[2] == '..':
                        del curdir[-1]
                    else:
                        curdir.append(thisline[2])
            else:
                if thisline[0] != 'dir':
                    for x in range(len(curdir)):
                        inlist['/'.join(curdir[0:x + 1]).replace('//', '/')] += int(thisline[0])
    outdf = pandas.DataFrame({'size': inlist.values()}, index=inlist.keys())
    return outdf


def p1(indf):
    """AoC 2022 Day 7 Part 1

    Find the size of directories to delete
    """
    return str(sum([x for x in indf[indf['size'] <= 100000]['size']]))


def p2(indf):
    """AoC 2022 Day 7 Part 2

    Free up disk space
    """
    freespace = 70000000 - indf.loc['/']['size']
    return [str(x) for x in sorted(indf['size'].tolist()) if freespace + x >= 30000000][0]


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
