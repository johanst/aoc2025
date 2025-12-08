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

    cidcnt = 0
    nets = {}
    bx2net = {}
    for i in range(len(a)):
        s = set()
        s.add(a[i])
        nets[cidcnt] = s
        bx2net[a[i]] = cidcnt
        cidcnt = cidcnt + 1
    # print(nets)
    # print(bx2net)
    for i in range(n):
        bx1, bx2 = a[d[i][1]], a[d[i][2]]
        # print(a[bx1], a[bx2])
        bx1nid = bx2net[bx1]
        bx2nid = bx2net[bx2]
        print(bx1nid, bx2nid)
        if bx1nid != bx2nid:
            print(f"join {bx1}|{bx2} => del {bx2nid}")
            for bx in nets[bx2nid]:
                nets[bx1nid].add(bx)
            bx2net[bx2] = bx1nid
            del nets[bx2nid]
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

part1("ex.txt", 10)
# part2("input.txt")
