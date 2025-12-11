#!/usr/bin/env python3
import heapq

def get_data(fname):
    a = {}
    with open(fname, "r") as file:
        for line in file:
            ws = line.strip().split()
            assert ws[0][-1] == ':'
            node = ws[0][:-1]
            paths = ws[1:]
            assert node not in a
            a[node] = paths
    return a

def num_paths_to_out(a, track):
    if track[-1] == 'out':
        return 1
    acc = 0
    for node in a[track[-1]]:
        # print(track)
        if node not in track:
            track.append(node)
            acc = acc + num_paths_to_out(a, track)
            track.pop()
    return acc

def part1(fname):
    a = get_data(fname)
    # print(a)
    acc = num_paths_to_out(a, ['you'])
    print(f"acc: {acc}")

def part2(fname):
    a = get_data(fname)
    acc = 0
    print(f"acc: {acc}")


part1("input.txt")
# part2("ex.txt")
