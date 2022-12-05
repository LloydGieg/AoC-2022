#!/usr/bin/env python3

import pandas
import re

day = 5
inputdir = '../InputFiles'

instre = re.compile(r'^move (\d+) from (\d+) to (\d+)$')
instructionsindex = 0


def initdf(infile):
    """AoC 2022 Day 5 Init

    Create a DataFrame from a text file.
    """
    global instructionsindex
    inlist = []
    with open(infile, 'r') as f:
        x, y = f.read().split('\n\n')
        if re.match(r'^.*? ([0-9]+)\s*$', x.splitlines()[-1]):
            for z in range(int(re.match(r'^.*? ([0-9]+)\s*$', x.splitlines()[-1]).group(1))):
                inlist.append([])
        instructionsindex = len(inlist)
        for z in x.split('\n')[:-1]:
            counter = 0
            for r in range(1, 35, 4):
                if z.ljust(35)[r] != ' ':
                    inlist[counter].insert(0, z[r])
                counter += 1
        for z in y.split('\n'):
            if instre.match(z):
                inlist.append([int(r) for r in instre.match(z).groups()])
    return pandas.DataFrame({0: inlist})


def p1(indf):
    """AoC 2022 Day 5 Part 1

    Move elements between lists.
    """
    indata = indf[0].apply(list.copy)
    for x, y, z in indata[instructionsindex:]:
        indata[z - 1].extend(indata[y - 1][:-x - 1:-1])
        del indata[y - 1][-x:]
    return ''.join([x[-1] for x in indata[:instructionsindex]])


def p2(indf):
    """AoC 2022 Day 5 Part 2

    Move elements between lists.
    """
    indata = indf[0].apply(list.copy)
    for x, y, z in indata[instructionsindex:]:
        indata[z - 1].extend(indata[y - 1][-x:])
        del indata[y - 1][-x:]
    return ''.join([x[-1] for x in indata[:instructionsindex]])


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
