#!/usr/bin/env python3

import pandas

day = 12
inputdir = '../InputFiles'

inlist = []
start = []
end = []
djikstra = []


def initdf(infile):
    """AoC 2022 Day 12 Init

    Create a DataFrame from a text file.
    """
    global inlist
    outlist = []
    with open(infile, 'r') as f:
        for x in f.read().split('\n'):
            outlist.append([y for y in x])
    return pandas.DataFrame(outlist)


def initinlist(indf):
    global inlist, start, end

    alphavalues = {chr(x + 96): x for x in range(1, 27)}

    inlist = indf.T.values.tolist()

    for x in range(len(inlist)):
        for y in range(len(inlist[x])):
            if inlist[x][y] == 'S':
                start = [x, y]
                inlist[x][y] = alphavalues['a']
            elif inlist[x][y] == 'E':
                end = [x, y]
                inlist[x][y] = alphavalues['z']
            else:
                inlist[x][y] = alphavalues[inlist[x][y]]


def p1(indf):
    """AoC 2022 Day 12 Part 1

    Find the distance from a single start point to a single end point
    """
    global inlist, djikstra, start, end

    initinlist(indf)

    djikstra = []
    unvisited = set()
    for x in range(len(inlist)):
        djikstra.append([])
        for y in range(len(inlist[x])):
            djikstra[x].append(999)
            unvisited.add(f"{x},{y}")

    djikstra[start[0]][start[1]] = 0

    while len(unvisited) > 0:
        tempvisited = unvisited.copy()
        changed = 0
        for z in sorted(tempvisited):
            x, y = z.split(',')
            x = int(x)
            y = int(y)
            if djikstra[x][y] == 999:
                continue
            if x > 0:
                if f"{x - 1},{y}" in unvisited:
                    if inlist[x][y] + 1 >= inlist[x - 1][y]:
                        if djikstra[x][y] + 1 < djikstra[x - 1][y]:
                            djikstra[x - 1][y] = djikstra[x][y] + 1
                            changed = 1
            if x < len(djikstra) - 1:
                if f"{x + 1},{y}" in unvisited:
                    if inlist[x][y] + 1 >= inlist[x + 1][y]:
                        if djikstra[x][y] + 1 < djikstra[x + 1][y]:
                            djikstra[x + 1][y] = djikstra[x][y] + 1
                            changed = 1
            if y > 0:
                if f"{x},{y - 1}" in unvisited:
                    if inlist[x][y] + 1 >= inlist[x][y - 1]:
                        if djikstra[x][y] + 1 < djikstra[x][y - 1]:
                            djikstra[x][y - 1] = djikstra[x][y] + 1
                            changed = 1
            if y < len(djikstra[x]) - 1:
                if f"{x},{y + 1}" in unvisited:
                    if inlist[x][y] + 1 >= inlist[x][y + 1]:
                        if djikstra[x][y] + 1 < djikstra[x][y + 1]:
                            djikstra[x][y + 1] = djikstra[x][y] + 1
                            changed = 1
            unvisited.remove(f"{x},{y}")
        if changed == 0:
            break

    return djikstra[end[0]][end[1]] or 999


def p2(indf):
    """AoC 2022 Day 12 Part 2

    Find the lowest distance from multiple start points to a single end point
    """
    global inlist, djikstra, start, end

    initinlist(indf)
    start = end

    djikstra = []
    unvisited = set()
    for x in range(len(inlist)):
        djikstra.append([])
        for y in range(len(inlist[x])):
            djikstra[x].append(999)
            unvisited.add(f"{x},{y}")

    djikstra[start[0]][start[1]] = 0

    while len(unvisited) > 0:
        tempvisited = unvisited.copy()
        changed = 0
        for z in sorted(tempvisited):
            x, y = z.split(',')
            x = int(x)
            y = int(y)
            if djikstra[x][y] == 999:
                continue
            if x > 0:
                if f"{x - 1},{y}" in unvisited:
                    if inlist[x][y] - 1 <= inlist[x - 1][y]:
                        if djikstra[x][y] + 1 < djikstra[x - 1][y]:
                            djikstra[x - 1][y] = djikstra[x][y] + 1
                            changed = 1
            if x < len(djikstra) - 1:
                if f"{x + 1},{y}" in unvisited:
                    if inlist[x][y] - 1 <= inlist[x + 1][y]:
                        if djikstra[x][y] + 1 < djikstra[x + 1][y]:
                            djikstra[x + 1][y] = djikstra[x][y] + 1
                            changed = 1
            if y > 0:
                if f"{x},{y - 1}" in unvisited:
                    if inlist[x][y] - 1 <= inlist[x][y - 1]:
                        if djikstra[x][y] + 1 < djikstra[x][y - 1]:
                            djikstra[x][y - 1] = djikstra[x][y] + 1
                            changed = 1
            if y < len(djikstra[x]) - 1:
                if f"{x},{y + 1}" in unvisited:
                    if inlist[x][y] - 1 <= inlist[x][y + 1]:
                        if djikstra[x][y] + 1 < djikstra[x][y + 1]:
                            djikstra[x][y + 1] = djikstra[x][y] + 1
                            changed = 1
            unvisited.remove(f"{x},{y}")
        if changed == 0:
            break

    lowpoints = []
    for x in range(len(inlist)):
        for y in range(len(inlist[x])):
            if inlist[x][y] == 1:
                if djikstra[x][y]:
                    lowpoints.append(djikstra[x][y])
    return min(lowpoints)


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
