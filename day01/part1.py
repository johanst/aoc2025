#!/usr/bin/env python3

def part1():
    pos = 50
    zeros = 0
    with open("input.txt", "r") as file:
        for line in file:
            l = line.strip()
            pos += 100
            if l[0] == 'L':
                pos -= int(l[1:])
            elif l[0] == 'R':
                pos += int(l[1:])
            else:
                assert "wtf"
            pos = pos % 100
            # print(f"{l}, => pos = {pos}")
            if pos == 0:
                zeros = zeros + 1
    print(f"Part1: Password = {zeros}")


def part2():
    pos = 50
    zeros = 0
    with open("input.txt", "r") as file:
        for line in file:
            l = line.strip()
            n = int(l[1:])
            zeros += n // 100
            n = n % 100
            if l[0] == 'L':
                if n > pos and pos != 0:
                    zeros += 1
                    # print("Passing zero")
                pos = pos + 100 - n
            elif l[0] == 'R':
                if n + pos > 100:
                    zeros += 1
                    # print("Passing zero")
                pos += n
            else:
                assert "wtf"
            pos = pos % 100
            print(f"{l}, => pos = {pos}")
            if pos == 0:
                zeros = zeros + 1
    print(f"Part2: Password = {zeros}")


part1()
part2()
