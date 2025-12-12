#!/usr/bin/env python3

def get_data(fname):
    a = []
    with open(fname, "r") as file:
        for line in file:
            l = line.strip()
            # ws = line.strip().split(',')
            # cs = (int(ws[0]), int(ws[1]), int(ws[2]))
            a.append(l)
    return a

def part1(fname):
    a = get_data(fname)
    acc = 0
    print(f"Sum: {acc}")

def part2(fname):
    a = get_data(fname)
    acc = 0
    print(f"Sum: {acc}")

part1("input.txt")
part2("input.txt")
