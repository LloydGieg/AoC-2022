#!/usr/bin/env python3

import pandas

day = 6
inputdir = '../InputFiles'


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
    inlist = [indata[x:x + 4] for x in range(len(indata) - 4)]
    for x in inlist:
        if len(set(x)) == 4:
            return str(inlist.index(x) + 4)


def p2(indf):
    """AoC 2022 Day 6 Part 2

    Find the first unique 14-character substring in a string
    """
    indata = indf[0][0]
    inlist = [indata[x:x + 14] for x in range(len(indata) - 14)]
    for x in inlist:
        if len(set(x)) == 14:
            return str(inlist.index(x) + 14)


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
