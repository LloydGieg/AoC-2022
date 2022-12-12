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
    return len([[] for w, x, y, z in indf.values.tolist() if len(set(range(w, x + 1)) & set(range(y, z + 1))) ==
                    min([len(set(range(w, x + 1))), len(set(range(y, z + 1)))])])


def p2(indf):
    """AoC 2022 Day 4 Part 2

    Find overlapping sections in a DataFrame.
    """
    return len([[] for w, x, y, z in indf.values.tolist() if len(set(range(w, x + 1)) & set(range(y, z + 1)))])


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
