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
    inlist = []
    with open(infile, 'r') as f:
        x, y = f.read().split('\n\n')
        if re.match(r'^.*? ([0-9]+)\s*$', x.splitlines()[-1]):
            for z in range(int(re.match(r'^.*? ([0-9]+)\s*$', x.splitlines()[-1]).group(1))):
                inlist.append([])
        globals()['instructionsindex'] = len(inlist)
        for z in x.split('\n')[:-1]:
            counter = 0
            for r in range(1, 35, 4):
                if z.ljust(35)[r] != ' ':
                    inlist[counter].insert(0, z[r])
                counter += 1
        for z in y.split('\n'):
            if instre.match(z):
                inlist.append([
                    int(instre.match(z).group(1)),
                    int(instre.match(z).group(2)),
                    int(instre.match(z).group(3))
                ])
    return pandas.DataFrame({0: inlist})


def p1(indf):
    """AoC 2022 Day 5 Part 1

    Move elements between lists.
    """
    returnlist = ''
    stacks = [x for x in indf[0][:instructionsindex]]
    instructions = [x for x in indf[0][instructionsindex:]]
    for x in instructions:
        qty, fromstack, tostack = x
        for y in range(qty):
            stacks[tostack - 1].append(stacks[fromstack - 1].pop())
    for x in stacks:
        returnlist += x[-1]
    return returnlist


def p2(indf):
    """AoC 2022 Day 5 Part 2

    Move elements between lists.
    """
    thisdf = initdf(f"{inputdir}/d{day}.txt")
    returnlist = ''
    stacks = [x for x in thisdf[0][:instructionsindex]]
    instructions = [x for x in thisdf[0][instructionsindex:]]
    for x in instructions:
        qty, fromstack, tostack = x
        stacks[tostack - 1].extend(stacks[fromstack - 1][-qty:])
        stacks[fromstack - 1] = stacks[fromstack - 1][:-qty]
    for x in stacks:
        returnlist += x[-1]
    return returnlist


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
