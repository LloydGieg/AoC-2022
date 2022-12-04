#!/usr/bin/env python3

import pandas

day = 2

them = ['A', 'B', 'C']
us = ['X', 'Y', 'Z']


def initdf(file):
    return pandas.read_csv(file, sep=' ', header=None)


def p1(indf):
    points = 0
    for x, y in [[a, b] for a, b in zip(indf[0], indf[1])]:
        points += us.index(y) + 1
        if them.index(x) == us.index(y):
            points += 3
        elif us[(them.index(x) + 1) % len(us)] == y:
            points += 6
    return points


def p2(indf):
    newus = []
    for x, y in [[a, b] for a, b in zip(indf[0], indf[1])]:
        newus.append(us[(them.index(x) + (us.index(y) - 1)) % len(us)])
    return p1(pandas.DataFrame(list(zip(indf[0].tolist(), newus))))


if __name__ == '__main__':
    df = initdf(f"../InputFiles/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
