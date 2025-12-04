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
    # poss = set()
    acc = 0
    for y0 in range(ly):
        for x0 in range(lx):
            count = 0
            cposs = set()
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
                        # cposs.add((y0, x0))
            if count < 4:
                acc = acc + 1
                # print(y0,x0,cposs)
                # for p in cposs:
                #     poss.add(p)
    # acc = len(poss)
    # for y in range(ly):
    #     for x in range(lx):
    #         if (y,x) in poss:
    #             print('x', end='')
    #         else:
    #             print(aa[y][x], end='')
    #     print()
    print(f"Sum: {acc}")

def part2(fname):
    aa = get_grid(fname)
    acc = 0
    print(f"Sum: {acc}")


part1("input.txt")
# part2("input.txt")
