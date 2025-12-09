#!/usr/bin/env python3

def get_data(fname):
    a = []
    with open(fname, "r") as file:
        for line in file:
            ws = line.strip().split(',')
            cs = (int(ws[0]), int(ws[1]))
            a.append(cs)
            assert(len(cs) == 2)
    return a

def part1(fname):
    a = get_data(fname)

    # get dists
    d = []
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            size = abs(((a[i][0]-a[j][0])) + 1)*(abs((a[i][1]-a[j][1]))+1)
            d.append((size, i, j))
    d.sort(reverse=True)
    print(f"Largest: {d[0][0]}")


def part2(fname):
    a = get_data(fname)
    print("hej")

part1("input.txt")
# part2("input.txt")
