#!/usr/bin/env python3

import pandas

day = 8
inputdir = '../InputFiles'

p2trees = {}


def initdf(infile):
    """AoC 2022 Day 8 Init

    Create a DataFrame from a text file.
    """
    outlist = []
    with open(infile, 'r') as f:
        for x in f.read().split('\n'):
            outlist.append([int(y) for y in x])
    return pandas.DataFrame(outlist)


def p1(indf):
    """AoC 2022 Day 8 Part 1

    Find the visible trees in the dataframe.
    """
    rows = indf.values.tolist()
    trees = set()

    for x in range(len(rows)):
        height = 0
        for y in range(len(rows[x])):
            if y == 0 or indf[x][y] > height:
                trees.add(f"{x},{y}")
                height = indf[x][y]
        height = 0
        for y in range(len(rows[x]) - 1, -1, -1):
            if y == len(rows[x])-1 or indf[x][y] > height:
                trees.add(f"{x},{y}")
                height = indf[x][y]

    for y in range(len(rows)):
        height = 0
        for x in range(len(rows[y])):
            if x == 0 or indf[x][y] > height:
                trees.add(f"{x},{y}")
                height = indf[x][y]
        height = 0
        for x in range(len(rows[y]) - 1, -1, -1):
            if x == len(rows[y])-1 or indf[x][y] > height:
                trees.add(f"{x},{y}")
                height = indf[x][y]

    return str(len(trees))


def checktree(indf, x, y):
    global p2trees
    p2trees[f"{x},{y}"] = 1
    # South
    visibility = 0
    for z in range(y+1, indf.shape[0]):
        visibility += 1
        if indf[x][z] >= indf[x][y]:
            break
    p2trees[f"{x},{y}"] *= visibility
    # North
    visibility = 0
    for z in range(y-1, -1, -1):
        visibility += 1
        if indf[x][z] >= indf[x][y]:
            break
    p2trees[f"{x},{y}"] *= visibility
    # East
    visibility = 0
    for z in range(x+1, indf.shape[1]):
        visibility += 1
        if indf[z][y] >= indf[x][y]:
            break
    p2trees[f"{x},{y}"] *= visibility
    # West
    visibility = 0
    for z in range(x-1, -1, -1):
        visibility += 1
        if indf[z][y] >= indf[x][y]:
            break
    p2trees[f"{x},{y}"] *= visibility


def p2(indf):
    """AoC 2022 Day 8 Part 2

    Find maximum visibility from the trees.
    """
    global p2trees

    for x in range(1, indf.shape[0]-1):
        for y in range(1, indf.shape[1]-1):
            checktree(indf, x, y)

    return str(max(p2trees.values()))


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
