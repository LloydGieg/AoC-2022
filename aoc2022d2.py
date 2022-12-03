#!/usr/bin/env python3

import pandas

them = ['A', 'B', 'C']
us = ['X', 'Y', 'Z']


def initdf(file):
    return pandas.read_csv(file, sep=' ', header=None)


def p1(df):
    points = 0
    for x, y in [[a, b] for a, b in zip(df[0], df[1])]:
        points += us.index(y) + 1
        if them.index(x) == us.index(y):
            points += 3
        elif us[(them.index(x) + 1) % len(us)] == y:
            points += 6
    return points


def p2(df):
    newus = []
    for x, y in [[a, b] for a, b in zip(df[0], df[1])]:
        newus.append(us[(them.index(x) + (us.index(y) - 1)) % len(us)])
    return p1(pandas.DataFrame(list(zip(df[0].tolist(), newus))))


if __name__ == '__main__':
    moves = initdf('Inputfiles/d2.txt')

    print(f"d2p1: {p1(moves)}")
    print(f"d2p2: {p2(moves)}")
