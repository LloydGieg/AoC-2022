#!/usr/bin/env python3

import pandas

day = 1


def initdf(file):
    returnlist = []
    with open(file) as f:
        for x in f.read().split('\n\n'):
            returnlist.append(sum(list([int(x) for x in x.split('\n')])))
    return pandas.DataFrame(returnlist)


def p1(indf):
    return indf[0].max()


def p2(indf):
    return sum(indf[0].nlargest(3).tolist())


if __name__ == '__main__':
    df = initdf(f"InputFiles/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
