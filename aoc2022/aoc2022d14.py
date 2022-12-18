#!/usr/bin/env python3

import pandas

day = 14
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 14 Init

    Create a DataFrame from a text file.
    """
    with open(infile, 'r') as f:
        lines = {'start': [], 'end': []}
        inlines = f.read().split('\n')
        for x in inlines:
            y = x.split(' -> ')
            for z in range(len(y) - 1):
                lines['start'].append([int(a) for a in y[z].split(',')])
                lines['end'].append([int(a) for a in y[z + 1].split(',')])
    return pandas.DataFrame(lines)


def p1(indf):
    """AoC 2022 Day 14 Part 1

    Count the sand in the maze
    """
    stuff = set()
    wstart = indf['start'].values.tolist()
    wend = indf['end'].values.tolist()
    for x in range(len(wstart)):
        if wstart[x][0] == wend[x][0]:
            for y in range(min(wstart[x][1], wend[x][1]), max(wstart[x][1], wend[x][1]) + 1):
                stuff.add(f"{wstart[x][0]},{y}")
            continue
        if wstart[x][1] == wend[x][1]:
            for y in range(min(wstart[x][0], wend[x][0]), max(wstart[x][0], wend[x][0]) + 1):
                stuff.add(f"{y},{wstart[x][1]}")
            continue
    maxwall = max([int(x.split(',')[1]) for x in stuff])
    full = 0
    counter = 0
    while full == 0:
        counter += 1
        sandloc = [500, 0]
        while 1:
            if sandloc[1] + 1 > maxwall:
                full = 1
                break
            if f"{sandloc[0]},{sandloc[1] + 1}" in stuff:
                if f"{sandloc[0] - 1},{sandloc[1] + 1}" in stuff:
                    if f"{sandloc[0] + 1},{sandloc[1] + 1}" in stuff:
                        stuff.add(f"{sandloc[0]},{sandloc[1]}")
                        break
                    else:
                        sandloc[0] += 1
                        sandloc[1] += 1
                else:
                    sandloc[0] -= 1
                    sandloc[1] += 1
            else:
                sandloc[1] += 1
    return counter - 1


def p2(indf):
    """AoC 2022 Day 14 Part 2

    Count the sand in the maze
    """
    stuff = set()
    wstart = indf['start'].values.tolist()
    wend = indf['end'].values.tolist()
    inc = 1000
    for x in range(len(wstart)):
        if wstart[x][0] == wend[x][0]:
            for y in range(min(wstart[x][1], wend[x][1]), max(wstart[x][1], wend[x][1]) + 1):
                stuff.add((wstart[x][0] * inc) + y)
            continue
        if wstart[x][1] == wend[x][1]:
            for y in range(min(wstart[x][0], wend[x][0]), max(wstart[x][0], wend[x][0]) + 1):
                stuff.add((y * inc) + wstart[x][1])
            continue
    maxwall = max([divmod(x, inc)[1] for x in stuff]) + 2
    counter = 0
    full = 0
    while full == 0:
        counter += 1
        sandloc = [500, 0]
        while 1:
            if ((499 * inc) + 1) in stuff and ((500 * inc) + 1) in stuff and ((501 * inc) + 1) in stuff:
                full = 1
                break
            if sandloc[1] + 1 == maxwall:
                stuff.add((sandloc[0] * inc) + sandloc[1])
                break
            if ((sandloc[0] * inc) + sandloc[1]) + 1 in stuff:
                if ((sandloc[0] - 1) * inc) + (sandloc[1] + 1) in stuff:
                    if ((sandloc[0] + 1) * inc) + (sandloc[1] + 1) in stuff:
                        stuff.add((sandloc[0] * inc) + sandloc[1])
                        break
                    else:
                        sandloc[0] += 1
                        sandloc[1] += 1
                else:
                    sandloc[0] -= 1
                    sandloc[1] += 1
            else:
                sandloc[1] += 1
    return counter


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
