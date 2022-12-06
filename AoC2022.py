#!/usr/bin/env python3

import time
import importlib

infiles = 'InputFiles'
aoc2022pkg = 'aoc2022'

timeunit = 'ms'
timeunits = {
    'seconds': 1,
    'ms': 1000,
    'ns': 1000000,
}

answerkey = {}
with open(f"{infiles}/answerkey.txt", 'r') as f:
    for x, y, z in [r.split(', ') for r in f.read().split('\n') if r != '']:
        answerkey[x] = [y, z]

incorrect = 0
start = time.time()
for x in answerkey:
    globals()[x] = importlib.import_module(f"{aoc2022pkg}.aoc2022{x}")
    df = getattr(globals()[x], 'initdf')(f"{infiles}/{x}.txt")
    for y in range(2):
        ystart = time.time()
        print(f"Day {x[1]} Part {y + 1}: ", end='')
        if getattr(globals()[x], f"p{y + 1}")(df) == answerkey[x][y]:
            print("Correct ", end='')
        else:
            incorrect += 1
            print("Incorrect ", end='')
        print(f"({int((time.time() - ystart) * timeunits[timeunit])} {timeunit})")
    print()

print(f"There are {incorrect} incorrect parts")
print(f"Total time: {int((time.time() - start) * timeunits[timeunit])} {timeunit}")
