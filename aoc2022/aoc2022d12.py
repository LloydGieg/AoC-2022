#!/usr/bin/env python3

import pandas

day = 12
inputdir = '../InputFiles'

inlist = []
start = []
end = []
dijkstra = []


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
    global inlist, dijkstra, start, end

    initinlist(indf)

    dijkstra = []
    unvisited = set()
    for x in range(len(inlist)):
        dijkstra.append([])
        for y in range(len(inlist[x])):
            dijkstra[x].append(999)
            unvisited.add(f"{x},{y}")

    dijkstra[start[0]][start[1]] = 0

    while len(unvisited) > 0:
        tempvisited = unvisited.copy()
        changed = 0
        for z in sorted(tempvisited):
            x, y = z.split(',')
            x = int(x)
            y = int(y)
            if dijkstra[x][y] == 999:
                continue
            if x > 0:
                if f"{x - 1},{y}" in unvisited:
                    if inlist[x][y] + 1 >= inlist[x - 1][y]:
                        if dijkstra[x][y] + 1 < dijkstra[x - 1][y]:
                            dijkstra[x - 1][y] = dijkstra[x][y] + 1
                            changed = 1
            if x < len(dijkstra) - 1:
                if f"{x + 1},{y}" in unvisited:
                    if inlist[x][y] + 1 >= inlist[x + 1][y]:
                        if dijkstra[x][y] + 1 < dijkstra[x + 1][y]:
                            dijkstra[x + 1][y] = dijkstra[x][y] + 1
                            changed = 1
            if y > 0:
                if f"{x},{y - 1}" in unvisited:
                    if inlist[x][y] + 1 >= inlist[x][y - 1]:
                        if dijkstra[x][y] + 1 < dijkstra[x][y - 1]:
                            dijkstra[x][y - 1] = dijkstra[x][y] + 1
                            changed = 1
            if y < len(dijkstra[x]) - 1:
                if f"{x},{y + 1}" in unvisited:
                    if inlist[x][y] + 1 >= inlist[x][y + 1]:
                        if dijkstra[x][y] + 1 < dijkstra[x][y + 1]:
                            dijkstra[x][y + 1] = dijkstra[x][y] + 1
                            changed = 1
            unvisited.remove(f"{x},{y}")
        if changed == 0:
            break

    return dijkstra[end[0]][end[1]] or 999


def p2(indf):
    """AoC 2022 Day 12 Part 2

    Find the lowest distance from multiple start points to a single end point
    """
    global inlist, dijkstra, start, end

    initinlist(indf)
    start = end

    dijkstra = []
    unvisited = set()
    for x in range(len(inlist)):
        dijkstra.append([])
        for y in range(len(inlist[x])):
            dijkstra[x].append(999)
            unvisited.add(f"{x},{y}")

    dijkstra[start[0]][start[1]] = 0

    while len(unvisited) > 0:
        tempvisited = unvisited.copy()
        changed = 0
        for z in sorted(tempvisited):
            x, y = z.split(',')
            x = int(x)
            y = int(y)
            if dijkstra[x][y] == 999:
                continue
            if x > 0:
                if f"{x - 1},{y}" in unvisited:
                    if inlist[x][y] - 1 <= inlist[x - 1][y]:
                        if dijkstra[x][y] + 1 < dijkstra[x - 1][y]:
                            dijkstra[x - 1][y] = dijkstra[x][y] + 1
                            changed = 1
            if x < len(dijkstra) - 1:
                if f"{x + 1},{y}" in unvisited:
                    if inlist[x][y] - 1 <= inlist[x + 1][y]:
                        if dijkstra[x][y] + 1 < dijkstra[x + 1][y]:
                            dijkstra[x + 1][y] = dijkstra[x][y] + 1
                            changed = 1
            if y > 0:
                if f"{x},{y - 1}" in unvisited:
                    if inlist[x][y] - 1 <= inlist[x][y - 1]:
                        if dijkstra[x][y] + 1 < dijkstra[x][y - 1]:
                            dijkstra[x][y - 1] = dijkstra[x][y] + 1
                            changed = 1
            if y < len(dijkstra[x]) - 1:
                if f"{x},{y + 1}" in unvisited:
                    if inlist[x][y] - 1 <= inlist[x][y + 1]:
                        if dijkstra[x][y] + 1 < dijkstra[x][y + 1]:
                            dijkstra[x][y + 1] = dijkstra[x][y] + 1
                            changed = 1
            unvisited.remove(f"{x},{y}")
        if changed == 0:
            break

    lowpoints = []
    for x in range(len(inlist)):
        for y in range(len(inlist[x])):
            if inlist[x][y] == 1:
                if dijkstra[x][y]:
                    lowpoints.append(dijkstra[x][y])
    return min(lowpoints)


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
