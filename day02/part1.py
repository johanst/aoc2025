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


def bad_id2(n):
    s = str(abs(n))
    l = len(s)
    if l == 0:
        return False
    for seq_len in range(1, l // 2 + 1):
        if l % seq_len != 0:
            continue
        ok = True
        for i in range(0, l // seq_len):
            if s[:seq_len] != s[seq_len*i:seq_len*(i+1)]:
                ok = False
                break
        if ok:
            return True
    return False

# print(bad_id2(2121212118))
# print(bad_id2(11))

def part2(fname):
    rs = get_ranges(fname)
    acc = 0
    for r in rs:
        for n in range(int(r[0]), int(r[1]) + 1):
            if bad_id2(n):
                # print(f"{r}: {n}")
                acc = acc + n
    print(f"Sum: {acc}")


part1("input.txt")
part2("input.txt")
