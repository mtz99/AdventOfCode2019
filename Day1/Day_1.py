import sys
import os


def main():
    calcd = []
    #Scan file path and read through it
    path = '/Users/matzh/Desktop/AdventOfCode2019/Day1/input.txt'
    with open(path) as File:
        x = File.readlines()
        for i in x:
            x = int(i)
            calcd.append(int(x/3)-2)
            print(calcd)
    File.close()
    print(sum(calcd))

    #print(x)

main()