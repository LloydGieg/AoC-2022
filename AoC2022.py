#!/usr/bin/env python3

import time

results = {
    'd1': [70296, 205381],
    'd2': [15691, 12989],
    'd3': [7903, 2548],
}

for x in results:
    globals()[x] = __import__(f"aoc2022{x}")
    df = getattr(globals()[x], 'initdf')(f"InputFiles/{x}.txt")
    print()
    for y in range(2):
        start = time.time()
        print(f"Day {x[1]} Part {y + 1}: ", end='')
        if getattr(globals()[x], f"p{y + 1}")(df) == results[x][y]:
            print("Correct ", end='')
        else:
            print("Incorrect ", end='')
        print(f"({int((time.time() - start) * 1000000)} ns)")
