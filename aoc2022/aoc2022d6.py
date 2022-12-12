#!/usr/bin/env python3

import pandas

day = 6
inputdir = '../InputFiles'

chars = 4


def initdf(infile):
    """AoC 2022 Day 6 Init

    Create a DataFrame from a text file.
    """
    with open(infile, 'r') as f:
        return pandas.DataFrame([f.readline()])


def p1(indf):
    """AoC 2022 Day 6 Part 1

    Find the first unique 4-character substring in a string
    """
    indata = indf[0][0]
    inlist = [indata[x:x + chars] for x in range(len(indata) - chars)]
    for x in inlist:
        if len(set(x)) == chars:
            return inlist.index(x) + chars


def p2(indf):
    """AoC 2022 Day 6 Part 2

    Find the first unique 14-character substring in a string
    """
    global chars
    chars = 14
    return p1(indf)


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
