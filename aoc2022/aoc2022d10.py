#!/usr/bin/env python3

import pandas

day = 10
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 10 Init

    Create a DataFrame from a text file.
    """
    return infile


def p1(indf):
    """AoC 2022 Day 10 Part 1

    """
    return str(indf)


def p2(indf):
    """AoC 2022 Day 10 Part 2

    """
    return str(indf)


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
