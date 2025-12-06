#!/usr/bin/env python3
from itertools import pairwise

def get_data(fname):
    ns = []
    ops = []
    with open(fname, "r") as file:
        for line in file:
            l = line.strip()
            try:
                nums = [int(w) for w in l.split()]
                ns.append(nums)
            except ValueError:
                ops = l.split()
    return ns, ops

def part1(fname):
    ns, ops = get_data(fname)
    acc = 0
    for i in range(len(ops)):
        assert ops[i] in "+*"
        n = 0 if ops[i] == '+' else 1
        for j in range(len(ns)):
            if ops[i] == '+':
                n = n + ns[j][i]
            else:
                n = n * ns[j][i]
        acc += n
    print(f"Sum: {acc}")

def get_data2(fname):
    ls = []
    ops = []
    with open(fname, "r") as file:
        for line in file:
            l = line.strip('\n')
            try:
                _ = int(l.split()[0])
                ls.append(l)
            except ValueError:
                ops = l.split()
    # assert every line is equal in length
    for r in ls:
        assert len(r) == len(ls[0])

    # find beginning of columns
    colbegs = [0]
    more_columns_to_search = True
    while more_columns_to_search:
        c = colbegs[-1] + 1
        while True:
            try:
                if all([l[c] == ' ' for l in ls]):
                    colbegs.append(c + 1)
                    break
            except IndexError:
                more_columns_to_search = False
                break
            c = c + 1
    assert len(colbegs) == len(ops)

    colbegs.append(len(ls[0]) + 1) # where the next number would have started
    # print(ls)
    # print(colbegs)
    nss = []
    for window in pairwise(colbegs):
        beg = window[0]
        sz = window[1] - beg - 1
        ns = []
        for c in range(beg, beg + sz):
            n = 0
            for l in ls:
                if l[c] != ' ':
                    n = n * 10 + int(l[c])
            ns.append(n)
        nss.append(ns)
    return nss, ops

def part2(fname):
    nss, ops = get_data2(fname)
    acc = 0
    for ns, op in zip(nss, ops):
        # print(ns, op)
        assert op in "+*"
        n = 0 if op == '+' else 1
        for part in ns:
            if op == '+':
                n = n + part
            else:
                n = n * part
        acc += n
    print(f"Sum: {acc}")

part1("input.txt")
part2("input.txt")
