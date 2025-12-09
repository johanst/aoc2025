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

def rec_size(a, i, j):
    size = abs(((a[i][0]-a[j][0])) + 1)*(abs((a[i][1]-a[j][1]))+1)
    return size

def part1(fname):
    a = get_data(fname)
    acc = 0
    print(f"Sum: {acc}")

def part2(fname):
    a = get_data(fname)
    acc = 0
    print(f"Sum: {acc}")

part1("ex.txt")
# part2("ex.txt")
