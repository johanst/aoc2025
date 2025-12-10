#!/usr/bin/env python3
import heapq

def get_data(fname):
    a = []
    with open(fname, "r") as file:
        for line in file:
            ws = line.strip().split(',')
            cs = (int(ws[0]), int(ws[1]))
            a.append(cs)
            assert(len(cs) == 2)
    return a

def part1(fname):
    a = get_data(fname)
    acc = 0
    print(f"acc: {acc}")

def part2(fname):
    a = get_data(fname)
    acc = 0
    print(f"acc: {acc}")


part1("ex.txt")
# part2("ex.txt")
