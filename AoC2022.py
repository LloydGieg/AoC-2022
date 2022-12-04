#!/usr/bin/env python3

import time
import importlib

results = {
    'd1': [70296, 205381],
    'd2': [15691, 12989],
    'd3': [7903, 2548],
    'd4': [560, 839],
}

infiles = 'InputFiles'
aoc2022pkg = 'aoc2022'

for x in results:
    globals()[x] = importlib.import_module(f"{aoc2022pkg}.aoc2022{x}")
    df = getattr(globals()[x], 'initdf')(f"{infiles}/{x}.txt")
    if list(results.keys()).index(x) > 0:
        print()
    for y in range(2):
        start = time.time()
        print(f"Day {x[1]} Part {y + 1}: ", end='')
        if getattr(globals()[x], f"p{y + 1}")(df) == results[x][y]:
            print("Correct ", end='')
        else:
            print("Incorrect ", end='')
        print(f"({int((time.time() - start) * 1000)} ms)")
