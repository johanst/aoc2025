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

def num_paths_to_out2(a, cache, from_node, to_node, have_dac, have_fft):
    if to_node == 'out':
        # print(track)
        if have_dac and have_fft:
            return 1
        else:
            return 0
    have_dac_next = to_node == 'dac' or have_dac
    have_fft_next = to_node == 'fft' or have_fft
    acc = 0
    for node_next in a[to_node]:
        # print(track)
        cache_key = (to_node, node_next, have_dac_next, have_fft_next)
        if cache_key in cache:
            acc = acc + cache[cache_key]
        else:
            acc = acc + num_paths_to_out2(a, cache, to_node, node_next, have_dac_next, have_fft_next)
    cache[(from_node, to_node, have_dac, have_fft)] = acc
    return acc

def part2(fname):
    a = get_data(fname)
    acc = 0
    cache = {}
    for node_next in a['svr']:
        acc = acc + num_paths_to_out2(a, cache, 'svr', node_next, False, False)
    print(f"acc: {acc}")

part1("input.txt")
part2("input.txt")
