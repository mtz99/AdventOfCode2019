import sys
import os

def main():
    path = '/Users/matzh/Desktop/AdventOfCode/Day1/input.txt'
    with open(path) as File:
        x = File.readlines()
    File.close()

    print(x)

main()