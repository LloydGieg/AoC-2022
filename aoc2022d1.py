#!/usr/bin/env python3

import pandas


def initdf(file):
    returnlist = []
    with open(file) as f:
        for x in f.read().split('\n\n'):
            returnlist.append(sum(list([int(x) for x in x.split('\n')])))
    return pandas.DataFrame(returnlist)


def p1(df):
    return df[0].max()


def p2(df):
    return sum(df[0].nlargest(3).tolist())


if __name__ == '__main__':
    elves = initdf('InputFiles/d1.txt')

    print(f"d1p1: {p1(elves)}")
    print(f"d1p2: {p2(elves)}")
