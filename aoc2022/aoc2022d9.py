#!/usr/bin/env python3

import pandas

day = 9
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 9 Init

    Create a DataFrame from a text file.
    """
    with open(infile, 'r') as f:
        outlist = []
        for x in f.read().split('\n'):
            outlist.append(x.split(' '))
    outdf = pandas.DataFrame(outlist)

    return outdf


def p1(indf):
    """AoC 2022 Day 9 Part 1

    Track the number of unique tail positions on a grid
    """
    moves = indf.values.tolist()
    hpos = [0, 0]
    tpos = [0, 0]
    places = {f"{tpos[0]},{tpos[1]}"}
    for x in moves:
        for y in range(int(x[1])):
            if x[0] == 'R':
                hpos[0] += 1
                if hpos[0] - tpos[0] > 1:
                    tpos = [hpos[0]-1, hpos[1]]
                    places.add(f"{tpos[0]},{tpos[1]}")
            elif x[0] == 'L':
                hpos[0] -= 1
                if tpos[0] - hpos[0] > 1:
                    tpos = [hpos[0]+1, hpos[1]]
                    places.add(f"{tpos[0]},{tpos[1]}")
            elif x[0] == 'U':
                hpos[1] += 1
                if hpos[1] - tpos[1] > 1:
                    tpos = [hpos[0], hpos[1]-1]
                    places.add(f"{tpos[0]},{tpos[1]}")
            elif x[0] == 'D':
                hpos[1] -= 1
                if tpos[1] - hpos[1] > 1:
                    tpos = [hpos[0], hpos[1]+1]
                    places.add(f"{tpos[0]},{tpos[1]}")
    return str(len(places))


positions = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
p2places = {'0,0'}


def move(hpos, tpos):
    if hpos[0] - tpos[0] > 1 and hpos[1] - tpos[1] > 1:
        tpos = [hpos[0]-1, hpos[1]-1]
    elif tpos[0] - hpos[0] > 1 and hpos[1] - tpos[1] > 1:
        tpos = [hpos[0]+1, hpos[1]-1]
    elif hpos[0] - tpos[0] > 1 and tpos[1] - hpos[1] > 1:
        tpos = [hpos[0]-1, hpos[1]+1]
    elif tpos[0] - hpos[0] > 1 and tpos[1] - hpos[1] > 1:
        tpos = [hpos[0]+1, hpos[1]+1]
    elif hpos[0] - tpos[0] > 1:
        tpos = [hpos[0]-1, hpos[1]]
    elif tpos[0] - hpos[0] > 1:
        tpos = [hpos[0]+1, hpos[1]]
    elif hpos[1] - tpos[1] > 1:
        tpos = [hpos[0], hpos[1]-1]
    elif tpos[1] - hpos[1] > 1:
        tpos = [hpos[0], hpos[1]+1]
    return tpos


def p2(indf):
    """AoC 2022 Day 9 Part 2

    Track the number of unique tail positions on a grid
    """
    moves = indf.values.tolist()
    global positions
    global p2places
    for x in moves:
        for y in range(int(x[1])):
            if x[0] == 'R':
                positions[0][0] += 1
            elif x[0] == 'L':
                positions[0][0] -= 1
            elif x[0] == 'U':
                positions[0][1] += 1
            elif x[0] == 'D':
                positions[0][1] -= 1
            for z in range(len(positions)-1):
                positions[z+1] = move(positions[z], positions[z+1])
            p2places.add(f"{positions[9][0]},{positions[9][1]}")
    return str(len(p2places))


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
