#!/usr/bin/env python3

import pandas

day = 3
inputdir = '../InputFiles'

idx = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))


def initdf(infile):
    """AoC 2022 Day 3 Init

    Create a DataFrame from a text file.
    """
    inlist = []
    with open(infile, 'r') as f:
        for x in f.read().split('\n'):
            inlist.append([x[:int(len(x)/2)], x[int(len(x)/2):]])
    return pandas.DataFrame(inlist)


def p1(indf):
    """AoC 2022 Day 3 Part 1

    Find the common element in two columns of a DataFrame.
    """
    points = 0
    for x, y in [[a, b] for a, b in zip(indf[0], indf[1])]:
        points += idx.index(list(set(x) & set(y))[0]) + 1
    return str(points)


def p2(indf):
    """AoC 2022 Day 3 Part 1

    Find the common element in three rows of a DataFrame.
    """
    points = 0
    elves = [(a + b) for a, b in zip(indf[0], indf[1])]
    while len(elves) > 0:
        group = []
        for x in range(3):
            group.append(elves.pop(-1))
        points += idx.index(list(set(group[0]) & set(group[1]) & set(group[2]))[0]) + 1
    return str(points)


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
