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

def really_bad_algorithm(rs):
    ro = []
    for i in range(len(rs)):
        # print(i, rs)
        r = rs[i]
        if r == (-1, -1):
            continue
        for j in range(i+1, len(rs)):
            rr = rs[j]
            if rr == (-1, -1):
                continue
            # print(r, rr)
            if r[1] < rr[0] or r[0] > rr[1]:
                # print("non-overlapping")
                continue
            if r[0] >= rr[0] and r[1] <= rr[1]:
                # print("r is contained by rr, discard r")
                r = (-1, -1)
                break
            elif r[0] <= rr[0] and r[0] >= rr[1]:
                # print("r constains rr, discard rr")
                rs[j] = (-1, -1)
            else :
                # print("overlapping, so extend r, discard rr")
                r = ((min(r[0], rr[0]) , max(r[1], rr[1])))
                rs[i] = r
                rs[j] = (-1, -1)
        if r != (-1, -1):
            ro.append(r)
    return ro

def part2(fname):
    rs, _ = get_data(fname)
    acc = 0
    ro = []
    while True:
        # print(rs)
        ro = really_bad_algorithm(rs)
        # print(ro)
        if rs == ro:
            break
        rs = ro
    for beg, end in ro:
        acc = acc + end - beg + 1
    print(f"Sum: {acc}")

# 344306344403172
# 330802486483965
def part2_again(fname):
    rs, _ = get_data(fname)
    heapq.heapify(rs)
    ro = []
    while rs:
        rg = heapq.heappop(rs)
        print(f"rg:          {rg}")
        while rs:
            rgn = rs[0]
            print(f"       rgn = {rgn}")
            if rgn[0] > rg[1]:
                print("    done")
                break
            rgn = heapq.heappop(rs)
            rg = (rg[0], rgn[1])
            print(f"    rg_new = {rg}")
        ro.append(rg)
    acc = sum([rg[1] - rg[0] + 1 for rg in ro])
    print(f"Sum: {acc}")

# part1("input.txt")
# part2("input.txt")
part2_again("input.txt")
