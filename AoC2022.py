#!/usr/bin/env python3

import time

import aoc2022d1 as d1
import aoc2022d2 as d2
import aoc2022d3 as d3

results = {
    'd1': [70296, 205381],
    'd2': [15691, 12989],
    'd3': [7903, 2548],
}

for x in results:
    df = getattr(globals()[x], 'initdf')(f"InputFiles/{x}.txt")
    print()
    for y in range(2):
        start = time.time()
        print(f"{x}p{y + 1}: ", end='')
        if getattr(globals()[x], f"p{y + 1}")(df) == results[x][y]:
            print("Correct ", end='')
        else:
            print("Incorrect ", end='')
        print(f"({int((time.time() - start) * 1000)} ms)")
