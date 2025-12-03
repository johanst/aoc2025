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
    # if len(idcs) > 1:
    #     return mx * 10 + mx
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



def part2(fname):
    rs = get_banks(fname)
    acc = 0
    print(f"Sum: {acc}")


part1("input.txt")
# part2("input.txt")
