#!/usr/bin/env python3
import heapq

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
    rs, _ = get_data(fname)
    heapq.heapify(rs)
    ro = []
    while rs:
        rg = heapq.heappop(rs)
        while rs:
            rgn = rs[0]
            if rgn[0] > rg[1]:
                break
            rgn = heapq.heappop(rs)
            rg = (rg[0], max(rgn[1], rg[1]))
        ro.append(rg)
    acc = sum([rg[1] - rg[0] + 1 for rg in ro])
    print(f"Sum: {acc}")

part1("input.txt")
part2("input.txt")
