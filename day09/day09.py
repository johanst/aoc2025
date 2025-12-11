#!/usr/bin/env python3
import heapq

def get_data(fname):
    a = []
    with open(fname, "r") as file:
        for line in file:
            ws = line.strip().split(',')
            cs = (int(ws[0]), int(ws[1]))
            a.append(cs)
            assert(len(cs) == 2)
    return a

def rec_size(a, i, j):
    size = abs(((a[i][0]-a[j][0])) + 1)*(abs((a[i][1]-a[j][1]))+1)
    return size

def part1(fname):
    a = get_data(fname)

    # get dists
    d = []
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            d.append((rec_size(a, i, j), i, j))
    d.sort(reverse=True)
    print(f"Largest: {d[0][0]}")

def t2h(t1, t2, is_horiz):
    assert(len(t1)==2)
    assert(len(t2)==2)
    xmin = min(t1[0], t2[0])
    xmax = max(t1[0], t2[0])
    ymin = min(t1[1], t2[1])
    return ((ymin, xmin, xmax), (t1, t2, is_horiz))

def part2(fname):
    a = get_data(fname)

    # get dists
    cands = []
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            if a[i][0] != a[j][0] and a[i][1] != a[j][1]:
                # candidates are rectangles with reds in opposite corners
                sz = rec_size(a, i, j)
                xmin = min(a[i][0],a[j][0])
                xmax = max(a[i][0],a[j][0])
                ymin = min(a[i][1],a[j][1])
                ymax = max(a[i][1],a[j][1])
                cands.append((sz, ((xmin,ymin), (xmax,ymax))))
    cands.sort(reverse=True)
    # print(cands)

    vs = []
    # keep track of horizontal endpoints to find out the vertical direction
    # before and after
    dirs = {} # (x, y) -> bool, Point -> direction (True=Down)
    for i in range(len(a)):
        print(a[i], a[j])
        j = (i + 1) % len(a)
        # sort border description so that either x or y is lower for the first corner
        # also keep track of whether we're dealing with a horizontal line as we
        # will lose that information later on
        if a[i][0] < a[j][0] or a[i][1] < a[j][1]:
            vs.append(t2h(a[i],a[j], a[i][0] != a[j][0]))
        else:
            vs.append(t2h(a[j] ,a[i], a[i][0] != a[j][0]))

        if a[i][1] == a[j][1]:
            # y is same => horizontal line
            h = ((len(a)) - 1 + i) % len(a)
            k = (j + 1) % len(a)
            assert a[h][0] == a[i][0] # last was vertical
            assert a[j][0] == a[k][0] # next is vertical
            dirs[a[i]] = a[i][1] > a[h][1]
            dirs[a[j]] = a[k][1] > a[j][1]
    heapq.heapify(vs)
    # print(vs)
    # print(dirs)

    rgs=[] # (y1u, y1d), ((x1l, x1r), (x2l, x2r) ... (xnl, xnr))
    while len(vs) > 0:
        # first extract all on same level
        (_, ((_, y), _, _)) = vs[0]
        rgnx = []
        rgny = []
        vl = None
        print("--ROW--")
        is_horiz_last = False
        while len(vs) > 0:
            (_, ((_,y1), _, _)) = vs[0]
            if y1 != y:
                break
            vn = heapq.heappop(vs)
            print(f"    {vn}")
            (_, ((x1,y1), (x2,y2), is_horiz)) = vn
            if is_horiz:
                # horizontal bar, add range then done
                rgnx.append((x1, x2))
                is_horiz_last = True
                print(f"    horiz {x1}-{x2}")
            else:
                if not vl:
                    print(f"    vert {x1}")
                    if dirs[(x1,y1)] != dirs[(x2,y2)] or not is_horiz_last:
                        # just rember every other vertical bar for regular walls
                        # but when preceded by a horizontal border and then
                        # moving vertically just like before we're just a
                        # continuation of a bordering wall so do not start a new
                        # area then
                        vl = vn
                        print(f"    vl = vn")
                else:
                    rgny.append(vn)
                    if not is_horiz_last:
                        # just a regular wall
                        (_, ((xl1,_), (xl2,_), _)) = vl
                        assert x1 == x2
                        assert xl1 == xl2
                        rgnx.append((xl1, x1))
                        vl = None
                    else:
                        if dirs[(x1,y1)] == dirs[(x2,y2)]:
                            # we previously started a new wall, but then came the horizontal
                            # bar and then we come to a wall moving in the same direction so
                            # we can just move the wall start (horizontal bar will cover the
                            # border)
                            vl = vn
                        else:
                            # we previously started a new wall, but now we're turning vertically
                            # so the complete wall has already been covered by the horizontal
                            # border
                            vl = None
                is_horiz_last = False
        print("rgnx: ", rgnx)
        print("rgny: ", rgny)
        assert vl == None
        yend = y + 1
        if len(vs) != 0:
            (_, ((_,yend), _, _)) = vs[0]
        yend = yend - 1
        rgs.append(((y, yend), rgnx))
        cnt_rgn_y = 0
        for vy in rgny:
            (_, ((x1,y1), (x2,y2), is_horiz)) = vy
            if yend == y2:
                continue
            assert yend < y2
            cnt_rgn_y = cnt_rgn_y + 1
            heapq.heappush(vs, t2h((x1,yend+1),(x2,y2), False))
        assert cnt_rgn_y % 2 == 0 # to verify we're only adding an even number of vertical walls
        print(f"=> rgs: {rgs[-1]}")
    # print(f"Largest: {cands[0][0]}")

# part1("input.txt")
part2("ex.txt")
