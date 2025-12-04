#!/usr/bin/env python3

def get_grid(fname):
    aa = []
    with open(fname, "r") as file:
        for line in file:
            l = line.strip()
            aa.append(l)
    return aa

def part1(fname):
    aa = get_grid(fname)
    ly = len(aa)
    lx = len(aa[0])
    acc = 0
    for y0 in range(ly):
        for x0 in range(lx):
            count = 0
            if aa[y0][x0] != '@':
                continue
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    x = x0 + dx
                    y = y0 + dy
                    if x < 0 or x >= lx or y < 0 or y >= ly or (dx == 0 and dy == 0):
                        continue
                    if aa[y][x] == '@':
                        count = count + 1
            if count < 4:
                acc = acc + 1
    print(f"Sum: {acc}")

def part2(fname):
    aa = get_grid(fname)
    ly = len(aa)
    lx = len(aa[0])
    r = set()
    for y0 in range(ly):
        for x0 in range(lx):
            if aa[y0][x0] == '@':
                r.add((y0,x0))
    totb = len(r)
    totl = totb
    while True:
        rr = set()
        for y0 in range(ly):
            for x0 in range(lx):
                if aa[y0][x0] != '@':
                    continue
                count = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        x = x0 + dx
                        y = y0 + dy
                        if dx == 0 and dy == 0:
                            continue
                        if (y, x) in r:
                            count = count + 1
                if count >= 4:
                    rr.add((y0,x0))
        r = rr
        if len(r) == totl:
            break
        totl = len(r)
    removed = totb - len(r)
    print(f"Removed: {removed}")

part1("input.txt")
part2("input.txt")
