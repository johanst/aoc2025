#!/usr/bin/env python3

def get_data(fname):
    a = []
    with open(fname, "r") as file:
        for line in file:
            ws = line.strip().split(',')
            cs = (int(ws[0]), int(ws[1]), int(ws[2]))
            a.append(cs)
            assert(len(cs) == 3)
    return a

def part1(fname, n):
    a = get_data(fname)

    # get dists
    d = []
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            dist = 0
            for c1, c2 in zip(a[i], a[j]):
                dist = dist + (c1 - c2) * (c1 - c2)
            d.append((dist, i, j))
    d.sort()

    nets = {}
    bx2net = {}
    for i in range(len(a)):
        s = set()
        s.add(a[i])
        nets[i] = s
    # print(nets)
    for i in range(n):
        bx1, bx2 = a[d[i][1]], a[d[i][2]]
        n1, n2 = -1, -1
        for sidx, s in nets.items():
            if bx1 in s:
                n1 = sidx
            if bx2 in s:
                n2 = sidx
            if n1 != -1 and n2 != -1:
                break
        assert n1 != -1 and n2 != -1
        if n1 != n2:
            for bx in nets[n2]:
                nets[n1].add(bx)
            del nets[n2]
    print(nets)
    ns = []
    for net in nets.values():
        ns.append(len(net))
    ns.sort(reverse=True)
    acc = ns[0] * ns[1] * ns[2]
    print(f"Sum: {acc}")

def part2(fname):
    a = get_data(fname)
    acc = 0
    print(f"Sum: {acc}")

# part1("ex.txt", 10)
part1("input.txt", 1000)
# part2("input.txt")
