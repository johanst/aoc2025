#!/usr/bin/env python3

def get_data(fname):
    rs = []
    aa = []
    rgs = True
    with open(fname, "r") as file:
        for line in file:
            l = line.strip()
            if rgs:
                if not l:
                    rgs = False
                else:
                    ws = l.split('-')
                    rs.append((int(ws[0]), int(ws[1])))
            else:
                aa.append(int(l))
    return rs, aa

def part1(fname):
    rs, aa = get_data(fname)
    acc = 0
    for a in aa:
        fresh = False
        for r in rs:
            if a >= r[0] and a <= r[1]:
                fresh = True
                break
        if fresh:
            acc = acc + 1
    print(f"Sum: {acc}")

def part2(fname):
    rs, aa = get_data(fname)
    acc = 0
    print(f"Sum: {acc}")

part1("input.txt")
# part2("input.txt")
