#!/usr/bin/env python3

import pandas

day = 7
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 7 Init

    Create a DataFrame from a text file.
    """
    return infile


def p1(indf):
    """AoC 2022 Day 6 Part 1

    """
    return indf


def p2(indf):
    """AoC 2022 Day 6 Part 2

    Find the first unique 14-character substring in a string
    """
    return indf


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
