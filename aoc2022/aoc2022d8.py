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

    return len(trees)


def p2(indf):
    """AoC 2022 Day 8 Part 2

    Find maximum visibility from the trees.
    """
    trees = {}
    for x in range(indf.shape[1]):
        for y in range(indf.shape[0]):
            trees[f"{x},{y}"] = 1

    for x in range(1, indf.shape[1]-1):
        for y in range(1, indf.shape[0]-1):
            height = indf[x][y]
            visibility = 0
            for z in range(y+1, indf.shape[0]):
                visibility += 1
                if indf[x][z] >= height:
                    break
            trees[f"{x},{y}"] *= (visibility or 1)

    for x in range(1, indf.shape[1]-1):
        for y in range(indf.shape[0]-2, 0, -1):
            height = indf[x][y]
            visibility = 0
            for z in range(y-1, -1, -1):
                visibility += 1
                if indf[x][z] >= height:
                    break
            trees[f"{x},{y}"] *= visibility

    for y in range(1, indf.shape[0]-1):
        for x in range(1, indf.shape[1]-1):
            height = indf[x][y]
            visibility = 0
            for z in range(x+1, indf.shape[1]):
                visibility += 1
                if indf[z][y] >= height:
                    break
            trees[f"{x},{y}"] *= visibility

    for y in range(1, indf.shape[0]-1):
        for x in range(indf.shape[1]-2, 0, -1):
            height = indf[x][y]
            visibility = 0
            for z in range(x-1, -1, -1):
                visibility += 1
                if indf[z][y] >= height:
                    break
            trees[f"{x},{y}"] *= visibility

    return max(trees.values())


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
