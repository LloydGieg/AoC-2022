#!/usr/bin/env python3

import pandas

day = 4
inputdir = '../InputFiles'


def initdf(infile):
    return infile


def p1(indf):
    return indf


def p2(indf):
    return indf


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
