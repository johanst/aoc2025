#!/usr/bin/env python3

def main():
    with open("input.txt", "r") as file:
        for line in file:
            print(line.strip())

main()
