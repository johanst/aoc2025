#!/usr/bin/env python3
import heapq
import re
import pulp

def get_data(fname):
    a = []
    p = re.compile('\[([.#]+)\](.*)\{(.*)\}.*')
    with open(fname, "r") as file:
        for line in file:
            l = line.strip()
            m = p.search(l)
            bconf = m.group(1)
            bps = []
            bpsw = m.group(2).split()
            for bp in bpsw:
                bps.append([int(num) for num in bp[1:-1].split(',')])
            jolts = [int(num) for num in m.group(3).split(',')]
            a.append((bconf, bps, jolts))
    return a

def bconf_str_to_num(bplist):
    n = 0
    for c in bplist:
        n = n * 2
        if c == '#':
            n = n + 1
    return n

assert bconf_str_to_num('.##.') == 6
assert bconf_str_to_num('.###.#') == 29

def bitnums_to_mask(eor_bitnums, num_bits):
    n = 0
    for bnum in eor_bitnums:
        n = n | (1 << (num_bits - 1 - bnum))
    return n

assert bitnums_to_mask((0,2), 4) == 10

def get_num_clicks(aa):
    ntarget = bconf_str_to_num(aa[0])
    masks = [bitnums_to_mask(bitnums, len(aa[0])) for bitnums in aa[1]]
    visited = {0: 0}
    hq = [(0, 0)]
    while len(hq) > 0:
        cost, n = heapq.heappop(hq)
        # print(f"evaluating n={n} ({n:b}), cost={cost}")
        if n == ntarget:
            return cost
        for mi, mask in enumerate(masks):
            ncand = n ^ mask
            cost_cand = cost + 1
            if ncand in visited:
                if visited[ncand] <= cost_cand:
                    continue
            # print(f"   press {aa[1][mi]} => n={ncand} ({ncand:b}), cost={cost_cand}")
            heapq.heappush(hq, (cost_cand, ncand))
            visited[ncand] = cost_cand
    return 0

assert get_num_clicks(('.###.#', [(0,1,2,3,4), (0,3,4), (0,1,2,4,5), (1,2)], (10,11,11,5,10,5))) == 2

def get_num_clicks_pulp(aa):
    print(aa)
    nbtns = len(aa[1])
    A = []
    b = aa[2]
    for cntidx in range(len(b)):
        eq = []
        for bid in range(nbtns):
            k = 1 if cntidx in aa[1][bid] else 0
            eq.append(k)
        A.append(eq)
    # print(A)
    # print(b)

    # An external equation solver was the only thing I could come up with,
    # but... I really dislike any task where I need to install something external
    # and where I can't reasonably implement the thing myself in any language.
    m, n = len(A), len(A[0])
    prob = pulp.LpProblem("MinSum", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(n)]
    # Objective: minimize sum
    prob += pulp.lpSum(x)
    # Constraints: A x = b
    for i in range(m):
        prob += pulp.lpSum(A[i][j] * x[j] for j in range(n)) == b[i]
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    solution = [int(pulp.value(var)) for var in x]
    # print(solution)
    # print(sum(solution))
    return sum(solution)

num_clicks = get_num_clicks_pulp(('.##.', [(3,), (1,3), (2,), (2,3), (0,2), (0,1)], [3,4,5,7]))
# print(num_clicks)
assert num_clicks == 10

def part1(fname):
    a = get_data(fname)
    acc = 0
    for aa in a:
        acc = acc + get_num_clicks(aa)
    print(f"Sum: {acc}")

def part2(fname):
    a = get_data(fname)
    # print(a)
    acc = 0
    for aa in a:
        print(aa)
        acc = acc + get_num_clicks_pulp(aa)
    print(f"Sum: {acc}")

part1("input.txt")
part2("input.txt")
