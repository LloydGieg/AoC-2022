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
    inlist = indf.T.values.tolist()
    trees = set()

    for x in range(indf.shape[1]):
        height = 0
        for y in range(indf.shape[0]):
            if y == 0 or int(inlist[x][y]) > height:
                trees.add(f"{x},{y}")
                height = int(inlist[x][y])
        height = 0
        for y in range(indf.shape[0]-1, -1, -1):
            if y == indf.shape[0]-1 or int(inlist[x][y]) > height:
                trees.add(f"{x},{y}")
                height = int(inlist[x][y])

    for y in range(indf.shape[0]):
        height = 0
        for x in range(indf.shape[1]):
            if x == 0 or int(inlist[x][y]) > height:
                trees.add(f"{x},{y}")
                height = int(inlist[x][y])
        height = 0
        for x in range(indf.shape[1]-1, -1, -1):
            if x == indf.shape[1]-1 or int(inlist[x][y]) > height:
                trees.add(f"{x},{y}")
                height = int(inlist[x][y])

    return len(trees)


def p2(indf):
    """AoC 2022 Day 8 Part 2

    Find maximum visibility from the trees.
    """
    inlist = indf.T.values.tolist()
    trees = []

    for x in range(len(inlist)):
        trees.append([])
        for y in range(len(inlist[x])):
            trees[x].append(1)

    besttree = 0

    for x in range(1, indf.shape[1]-1):
        for y in range(1, len(inlist[x])-1):
            height = inlist[x][y]
            visibility = 0
            for z in range(y+1, len(inlist[x])):
                visibility += 1
                if indf[x][z] >= height:
                    break
            trees[x][y] *= (visibility or 1)
            if trees[x][y] > besttree:
                besttree = trees[x][y]
        for y in range(len(inlist[x])-2, 0, -1):
            height = inlist[x][y]
            visibility = 0
            for z in range(y-1, -1, -1):
                visibility += 1
                if indf[x][z] >= height:
                    break
            trees[x][y] *= (visibility or 1)
            if trees[x][y] > besttree:
                besttree = trees[x][y]

    for y in range(1, indf.shape[0]-1):
        for x in range(1, indf.shape[1]-1):
            height = inlist[x][y]
            visibility = 0
            for z in range(x+1, indf.shape[1]):
                visibility += 1
                if indf[z][y] >= height:
                    break
            trees[x][y] *= (visibility or 1)
            if trees[x][y] > besttree:
                besttree = trees[x][y]
        for x in range(indf.shape[1]-2, 0, -1):
            height = inlist[x][y]
            visibility = 0
            for z in range(x-1, -1, -1):
                visibility += 1
                if indf[z][y] >= height:
                    break
            trees[x][y] *= (visibility or 1)
            if trees[x][y] > besttree:
                besttree = trees[x][y]

    return besttree


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
