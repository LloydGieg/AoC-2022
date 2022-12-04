#!/usr/bin/env python3

import pandas

day = 2
inputdir = '../InputFiles'

them = ['A', 'B', 'C']
us = ['X', 'Y', 'Z']


def initdf(infile):
    """AoC 2022 Day 2 Init

    Create a DataFrame from a text file.
    """
    return pandas.read_csv(infile, sep=' ', header=None)


def p1(indf):
    """AoC 2022 Day 2 Part 1

    Play a Rock/Paper/Scissors game.
    """
    points = 0
    for x, y in [[a, b] for a, b in zip(indf[0], indf[1])]:
        points += us.index(y) + 1
        if them.index(x) == us.index(y):
            points += 3
        elif us[(them.index(x) + 1) % len(us)] == y:
            points += 6
    return points


def p2(indf):
    """AoC 2022 Day 2 Part 2

    Reformat the input DataFrame and submit to Rock/Paper/Scissors game Part 1.
    """
    newus = []
    for x, y in [[a, b] for a, b in zip(indf[0], indf[1])]:
        newus.append(us[(them.index(x) + (us.index(y) - 1)) % len(us)])
    newdf = pandas.DataFrame(list(zip(indf[0].tolist(), newus)))
    return p1(newdf)


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
