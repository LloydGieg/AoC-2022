#!/usr/bin/env python3

import pandas
import hashlib

day = 10
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 10 Init

    Create a DataFrame from a text file.
    """
    with open(infile, 'r') as f:
        outdf = pandas.DataFrame([x.split(' ') for x in f.read().split('\n')])
    return outdf


def p1(indf):
    """AoC 2022 Day 10 Part 1

    Find the sum of the signal strengths
    """
    inlist = indf.values.tolist()
    reg = 1
    cycle = 0
    vals = []
    for x in range(len(inlist)):
        if inlist[x][0] == 'noop':
            cycle += 1
            if (cycle - 20) % 40 == 0:
                vals.append(reg * cycle)
        elif inlist[x][0] == 'addx':
            for y in range(2):
                cycle += 1
                if (cycle - 20) % 40 == 0:
                    vals.append(reg * cycle)
            reg += int(inlist[x][1])
    return sum(vals)


def p2(indf):
    """AoC 2022 Day 10 Part 2

    Draw an image on a CRT
    """
    inlist = indf.values.tolist()
    reg = 1
    cycle = 0
    returnstring = '\n'
    for x in range(len(inlist)):
        if inlist[x][0] == 'noop':
            if cycle % 40 in range(reg - 1, reg + 2):
                returnstring += '#'
            else:
                returnstring += '.'
            cycle += 1
            if cycle % 40 == 0:
                returnstring += '\n'
        elif inlist[x][0] == 'addx':
            for y in range(2):
                if cycle % 40 in range(reg - 1, reg + 2):
                    returnstring += '#'
                else:
                    returnstring += '.'
                cycle += 1
                if cycle % 40 == 0:
                    returnstring += '\n'
            reg += int(inlist[x][1])
    # Note you'll have to "print(returnstring)" to see the answer here
    # print(returnstring)
    return hashlib.md5(returnstring.encode()).hexdigest()


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
