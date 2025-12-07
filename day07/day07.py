#!/usr/bin/env python3

def get_data(fname):
    a = []
    with open(fname, "r") as file:
        for line in file:
            a.append(line.strip())
    return a, a[0].find('S')

def part1(fname):
    a, s = get_data(fname)
    acc = 0
    b = set([s])
    for r in a[1:]:
        bn = set()
        beg = 0
        while True:
            idx = r.find('^', beg)
            if idx == -1:
                break
            if idx in b:
                acc = acc + 1
                b.remove(idx)
                bn.add(idx-1)
                bn.add(idx+1)
            beg = idx + 1
        b = b | bn
    print(f"Sum: {acc}")

def part2(fname):
    a, s = get_data(fname)
    acc = 0
    print(f"Sum: {acc}")

part1("input.txt")
# part2("input.txt")
