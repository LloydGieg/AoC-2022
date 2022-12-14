#!/usr/bin/env python3

import pandas
import json

day = 13
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 13 Init

    Create a DataFrame from a text file.
    """
    with open(infile, 'r') as f:
        packets = f.read().split('\n\n')
        outlist = {'left': [], 'right': []}
        for x in packets:
            y, z = x.split('\n')
            outlist['left'].append(y)
            outlist['right'].append(z)
    return pandas.DataFrame(outlist)


def cmplist(a, b):
    result = ''
    for x in range(max(len(a), len(b))):
        if result != '':
            break
        try:
            a[x]
        except IndexError:
            result = 'right'
            continue
        try:
            b[x]
        except IndexError:
            result = 'wrong'
            continue
        if isinstance(a[x], list):
            if isinstance(b[x], list):
                result = cmplist(a[x], b[x])
            else:
                result = cmplist(a[x], [b[x]])
        elif isinstance(b[x], list):
            result = cmplist([a[x]], b[x])
        else:
            if a[x] < b[x]:
                result = 'right'
                continue
            elif a[x] > b[x]:
                result = 'wrong'
                continue
    return result


def p1(indf):
    """AoC 2022 Day 13 Part 1

    Count the packets in the correct order
    """
    outlist = []
    left = json.loads(indf['left'].to_json())
    right = json.loads(indf['right'].to_json())
    for x in left:
        inleft = json.loads(left[x])
        inright = json.loads(right[x])
        result = cmplist(inleft, inright)
        if result != 'wrong':
            outlist.append(int(int(x) + 1))
    return sum(outlist)


def p2(indf):
    """AoC 2022 Day 13 Part 2

    Put all the packets in order and return the product of the divider packet indices
    """
    d1 = '[[2]]'
    d2 = '[[6]]'
    inlist = indf['left'].tolist() + indf['right'].tolist() + [d1] + [d2]
    outlist = json.loads(json.dumps({str(x): y for x, y in enumerate(inlist)}))
    change = 1
    while change == 1:
        change = 0
        for x in range(0, len(outlist) - 1, 2):
            outcopy = outlist.copy()
            if cmplist(json.loads(outcopy[str(x)]), json.loads(outcopy[str(x + 1)])) == 'wrong':
                change = 1
                outlist[str(x)], outlist[str(x + 1)] = outlist[str(x + 1)], outlist[str(x)]
        for x in range(1, len(outlist) - 2, 2):
            outcopy = outlist.copy()
            if cmplist(json.loads(outcopy[str(x)]), json.loads(outcopy[str(x + 1)])) == 'wrong':
                change = 1
                outlist[str(x)], outlist[str(x + 1)] = outlist[str(x + 1)], outlist[str(x)]
    return (list(outlist.values()).index(d1) + 1) * (list(outlist.values()).index(d2) + 1)


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
