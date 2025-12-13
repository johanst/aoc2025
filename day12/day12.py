#!/usr/bin/env python3

def get_data(fname):
    a = []
    with open(fname, "r") as file:
        for line in file:
            l = line.strip()
            if 'x' in l:
                lp = l.split(':')
                wl = lp[0].split('x')
                width, length = int(wl[0]), int(wl[1])
                npack = [int(w) for w in lp[1].split()]
                a.append((width, length, npack))
    return a

def part1(fname):
    a = get_data(fname)
    ps = []
    for pdata in a:
        width, height, packets = pdata
        area = width * height
        area_required = sum(packets) * 9
        ps.append((area_required / area, area, area_required))

    ps.sort()
    for p in ps:
        print(p)
    acc = sum([1 for p in ps if p[0] < 1.1])
    print(f"Sum: {acc}")

def part2(fname):
    a = get_data(fname)
    acc = 0
    print(f"Sum: {acc}")

part1("input.txt")
# part2("input.txt")
