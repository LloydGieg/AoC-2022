#!/usr/bin/env python3

import pandas

day = 4
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 4 Init

    Create a DataFrame from a text file.
    """
    return pandas.read_csv(infile, sep='[-,]', engine='python', header=None)


def p1(indf):
    """AoC 2022 Day 4 Part 1

    Find overlapping sections in a DataFrame.
    """
    overlaps = 0
    for x in zip(indf[0], indf[1], indf[2], indf[3]):
        y, z = [set(range(x[0], x[1] + 1)), set(range(x[2], x[3] + 1))]
        if len(y & z) == min([len(y), len(z)]):
            overlaps += 1
    return overlaps


def p2(indf):
    """AoC 2022 Day 4 Part 2

    Find overlapping sections in a DataFrame.
    """
    overlaps = 0
    for x in zip(indf[0], indf[1], indf[2], indf[3]):
        y, z = [set(range(x[0], x[1] + 1)), set(range(x[2], x[3] + 1))]
        if len(y & z):
            overlaps += 1
    return overlaps


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
