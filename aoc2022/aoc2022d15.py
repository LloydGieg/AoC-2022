#!/usr/bin/env python3

import pandas
import re

day = 15
inputdir = '../InputFiles'


def initdf(infile):
    """AoC 2022 Day 15 Init

    Create a DataFrame from a text file.
    """
    linere = re.compile(r'^Sensor at x=([0-9\-]+), y=([0-9\-]+): closest beacon is at x=([0-9\-]+), y=([0-9\-]+)$')
    outlist = {'sx': [], 'sy': [], 'bx': [], 'by': [], 'dist': []}
    with open(infile, 'r') as f:
        for x in f.read().split('\n'):
            thissx, thissy, thisbx, thisby = linere.match(x).groups()
            outlist['sx'].append(int(thissx))
            outlist['sy'].append(int(thissy))
            outlist['bx'].append(int(thisbx))
            outlist['by'].append(int(thisby))
            outlist['dist'].append(abs(int(thissx) - int(thisbx)) + abs(int(thissy) - int(thisby)))
    return pandas.DataFrame(outlist)


def p1(indf):
    """AoC 2022 Day 15 Part 1

    Find where the beacons can't be
    """
    occupado = set()
    testrow = 2000000
    sx = indf['sx'].values.tolist()
    sy = indf['sy'].values.tolist()
    bx = indf['bx'].values.tolist()
    by = indf['by'].values.tolist()
    dist = indf['dist'].values.tolist()
    for x in range(len(sx)):
        if testrow not in range(
            sy[x] - dist[x],
            sy[x] + dist[x] + 1
        ):
            continue
        ydist = abs(testrow - sy[x])
        for y in range(
            sx[x] - (dist[x] - ydist),
            sx[x] + (dist[x] - ydist) + 1
        ):
            occupado.add(y)
        if by[x] == testrow:
            occupado.remove(bx[x])
    return len(occupado)


def border(xx, xy, xdist, yx, yy, ydist):
    returnset = set()
    if xx <= yx:
        if xy <= yy:
            if xdist <= ydist:
                counter = 0
                for x in range(xx, yx + 1):
                    thisx = xx + counter
                    thisy = xy + xdist + 1 - counter
                    returnset.add(f"{thisx},{thisy}")
                    counter += 1
            else:
                counter = 0
                for x in range(yx, xx - 1, -1):
                    thisx = yx - counter
                    thisy = yy - ydist - 1 + counter
                    returnset.add(f"{thisx},{thisy}")
                    counter += 1
        else:
            if xdist <= ydist:
                counter = 0
                for x in range(xx, yx + 1):
                    thisx = xx + counter
                    thisy = xy - xdist - 1 + counter
                    returnset.add(f"{thisx},{thisy}")
                    counter += 1
            else:
                counter = 0
                for x in range(yx, xx - 1, -1):
                    thisx = yx - counter
                    thisy = yy + ydist + 1 - counter
                    returnset.add(f"{thisx},{thisy}")
                    counter += 1
        return returnset
    else:
        return border(yx, yy, ydist, xx, xy, xdist)


def p2(indf):
    """AoC 2022 Day 15 Part 2

    Find the missing beacon.
    """
    sx = indf['sx'].values.tolist()
    sy = indf['sy'].values.tolist()
    dist = indf['dist'].values.tolist()
    pairs = []
    for x in range(len(sx)):
        for y in range(x + 1, len(sx)):
            thisdist = abs(sx[x] - sx[y]) + abs(sy[x] - sy[y])
            if thisdist == dist[x] + dist[y] + 2:
                pairs.append([x, y])
    for x in range(len(pairs) - 1):
        xpossible = border(sx[pairs[x][0]], sy[pairs[x][0]], dist[pairs[x][0]],
                               sx[pairs[x][1]], sy[pairs[x][1]], dist[pairs[x][1]])
        if len(xpossible) > 0:
            for y in range(x + 1, len(pairs)):
                if len({pairs[x][0], pairs[x][1], pairs[y][0], pairs[y][1]}) < 4:
                    continue
                ypossible = border(sx[pairs[y][0]], sy[pairs[y][0]], dist[pairs[y][0]],
                                   sx[pairs[y][1]], sy[pairs[y][1]], dist[pairs[y][1]])
                if len(ypossible) > 0:
                    result = list(xpossible & ypossible)
                    if len(result) == 1:
                        return int(result[0].split(',')[0]) * 4000000 + int(result[0].split(',')[1])


if __name__ == '__main__':
    df = initdf(f"{inputdir}/d{day}.txt")

    for i in range(2):
        j = globals()[f"p{i + 1}"]
        print(f"Day {day} Part {i + 1}: {j(df)}")
