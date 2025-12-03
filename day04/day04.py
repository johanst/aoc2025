#!/usr/bin/env python3

def get_banks(fname):
    aa = []
    with open(fname, "r") as file:
        for line in file:
            l = line.strip()
            a = [int(c) for c in l]
            aa.append(a)
    return aa

def get_max_jolt(a):
    idcs = []
    mx = -1
    for i, n in enumerate(a[:-1]):
        if n > mx:
            idcs = [i]
            mx = n
        elif n == mx:
            idcs.append(i)
            mx = n
    mx2 = -1
    for n in a[idcs[0]+1:]:
        if n > mx2:
            mx2 = n
    return mx * 10 + mx2

def part1(fname):
    aa = get_banks(fname)
    acc = 0
    for a in aa:
        mx = get_max_jolt(a)
        # print(mx)
        acc = acc + mx
    print(f"Sum: {acc}")

def get_max_jolt_12(a):
    jolt = 0
    bidx = 0
    for ndig in range(12):
        mx = -1
        nidx = -1
        for i, n in enumerate(a[bidx:len(a) - 11 + ndig]):
            if n > mx:
                mx = n
                nidx = i + bidx + 1
        jolt = jolt * 10 + mx
        bidx = nidx
        # print(mx, bidx, len(a) - ndig)
    return jolt

def part2(fname):
    aa = get_banks(fname)
    acc = 0
    # get_max_jolt_12(aa[0])
    # return
    for a in aa:
        mx = get_max_jolt_12(a)
        # print(mx)
        acc = acc + mx
    print(f"Sum: {acc}")


part1("input.txt")
part2("input.txt")
