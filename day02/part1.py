#!/usr/bin/env python3

def get_ranges(fname):
    with open(fname, "r") as file:
        for line in file:
            l = line.strip()
            ranges = []
            return [w.split('-') for w in l.split(',')]

def bad_id(n):
    s = str(abs(n))
    if len(s) == 0 or (len(s) & 1) == 1:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def part1(fname):
    rs = get_ranges(fname)
    acc = 0
    for r in rs:
        for n in range(int(r[0]), int(r[1]) + 1):
            if bad_id(n):
                # print(f"{r}: {n}")
                acc = acc + n
    print(f"Sum: {acc}")


def part2():
    print(f"Part2: Password = {zeros}")


part1("input.txt")
# part2()
