#!/usr/bin/env python3

import pandas
import re

day = 11
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 11 Init

    Create a DataFrame from a text file.
    """
    monkeyre = re.compile(r'^Monkey (\d+):$')
    startingitemsre = re.compile(r'^\s+Starting items: (.*)$')
    operationre = re.compile(r'^\s+Operation: new = old (.*)$')
    divisiblebyre = re.compile(r'^\s+Test: divisible by (\d+)$')
    iftruere = re.compile(r'^\s+If true: throw to monkey (\d+)$')
    iffalsere = re.compile(r'^\s+If false: throw to monkey (\d+)$')

    outlist = {'monkey': [], 'items': [], 'operation': [], 'divisibleby': [], 'iftrue': [], 'iffalse': []}
    with open(infile, 'r') as f:
        monkeys = f.read().split('\n\n')
        for monkey in monkeys:
            x = monkey.split('\n')
            outlist['monkey'].append(monkeyre.match(x[0]).group(1))
            outlist['items'].append(startingitemsre.match(x[1]).group(1))
            outlist['operation'].append(operationre.match(x[2]).group(1))
            outlist['divisibleby'].append(divisiblebyre.match(x[3]).group(1))
            outlist['iftrue'].append(iftruere.match(x[4]).group(1))
            outlist['iffalse'].append(iffalsere.match(x[5]).group(1))

    return pandas.DataFrame(outlist).set_index('monkey')


def p1(indf):
    """AoC 2022 Day 11 Part 1

    Chase monkeys
    """
    indict = indf.T.to_dict('list')
    for monkey in indict:
        indict[monkey][0] = [int(x) for x in indict[monkey][0].split(', ')]
        indict[monkey][1] = [x for x in indict[monkey][1].split(' ')]
        indict[monkey][2] = int(indict[monkey][2])
        indict[monkey][3] = indict[monkey][3]
        indict[monkey][4] = indict[monkey][4]
        indict[monkey].append(0)
    for _ in range(20):
        for monkey in indict:
            items = [x for x in indict[monkey][0]]
            operation = [x for x in indict[monkey][1]]
            divisibleby = indict[monkey][2]
            iftrue = indict[monkey][3]
            iffalse = indict[monkey][4]
            for x in items:
                indict[monkey][5] += 1
                indict[monkey][0].remove(x)
                worrylevel = x
                if operation[0] == '*':
                    if operation[1] == 'old':
                        worrylevel *= worrylevel
                    else:
                        worrylevel *= int(operation[1])
                elif operation[0] == '+':
                    if operation[1] == 'old':
                        worrylevel += worrylevel
                    else:
                        worrylevel += int(operation[1])
                worrylevel = int(worrylevel / 3)
                if worrylevel % divisibleby == 0:
                    indict[iftrue][0].append(worrylevel)
                else:
                    indict[iffalse][0].append(worrylevel)
    outresult = 1
    for x in range(2):
        outresult *= sorted([indict[y][5] for y in indict], reverse=True)[x]
    return outresult


def p2(indf):
    """AoC 2022 Day 11 Part 2

    Chase monkeys
    """
    indict = indf.T.to_dict('list')
    lcm = 1
    for monkey in indict:
        indict[monkey][0] = [int(x) for x in indict[monkey][0].split(', ')]
        indict[monkey][1] = [x for x in indict[monkey][1].split(' ')]
        indict[monkey][2] = int(indict[monkey][2])
        lcm *= indict[monkey][2]
        indict[monkey][3] = indict[monkey][3]
        indict[monkey][4] = indict[monkey][4]
        indict[monkey].append(0)
    for r in range(10000):
        for monkey in indict:
            items = [x for x in indict[monkey][0]]
            indict[monkey][5] += len(items)
            indict[monkey][0] = []
            operation, inoperand = [x for x in indict[monkey][1]]
            divisor = indict[monkey][2]
            iftrue = indict[monkey][3]
            iffalse = indict[monkey][4]
            for x in items:
                worrylevel = x
                if inoperand == 'old':
                    operand = worrylevel
                else:
                    operand = int(inoperand)
                if operation == '*':
                    if (worrylevel * operand) % divisor == 0:
                        indict[iftrue][0].append((worrylevel * operand) % lcm)
                    else:
                        indict[iffalse][0].append((worrylevel * operand) % lcm)
                elif operation == '+':
                    if (worrylevel + operand) % divisor == 0:
                        indict[iftrue][0].append((worrylevel + operand) % lcm)
                    else:
                        indict[iffalse][0].append((worrylevel + operand) % lcm)
    outresult = 1
    for x in range(2):
        outresult *= sorted([indict[y][5] for y in indict], reverse=True)[x]
    return outresult


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
