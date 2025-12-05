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
    rs, _ = get_data(fname)
    acc = 0
    ro = rs
    for r in rs:
        rn = []
        for rr in ro:
            if r[1] < rr[0]:
                # r to the left of rr, keep both
                rn.append(r)
                rn.append(rr)
            elif r[0] > rr[1]:
                # r to the right of rr, keep both
                rn.append(r)
                rn.append(rr)
            elif r[0] >= rr[0] and r[1] <= rr[1]:
                # r is contained by rr, only keep rr
                rn.append(rr)
            elif r[0] <= rr[0] and r[0] >= rr[1]:
                # r constains rr, only keep r
                rn.append(r)
            else:
                # overlapping, so merge
                rn.append((min(r[0], rr[0]), (max(r[1], rr[1])))
        ro = rn
    for beg, end in ro:
        acc = acc + end - beg + 1
    print(f"Sum: {acc}")

# part1("input.txt")
part2("ex.txt")
