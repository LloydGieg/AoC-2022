#!/usr/bin/env python3

import pandas

day = 1
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 1 Init

    Create a DataFrame from a text file.
    """
    returnlist = []
    with open(infile) as f:
        for x in f.read().split('\n\n'):
            returnlist.append(sum(list([int(x) for x in x.split('\n')])))
    return pandas.DataFrame(returnlist)


def p1(indf):
    """AoC 2022 Day 1 Part 1

    Return the maximum value from a single-column DataFrame.
    """
    return indf[0].max()


def p2(indf):
    """AoC 2022 Day 1 Part 2

    Return the sum of the largest three values in a single-column DataFrame.
    """
    return sum(indf[0].nlargest(3).tolist())


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
