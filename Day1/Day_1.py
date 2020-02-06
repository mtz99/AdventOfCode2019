import sys
import os

def main():
    #Scan file path and read through it
    path = '/Users/matzh/Desktop/AdventOfCode2019/Day1/input.txt'
    with open(path) as File:
        xval = list(map(int, File.read().strip().split()))
    File.close()
    
    final = [0,0]
    
    #Part 1
    #calcd = []
    for i in xval:
        final[0] += int(i/3-2)
    #final[0] += sum(calcd)
    
    #Part 2
    for i in xval:
        while(int(i/3-2) > 0):
            i = int(i/3-2)
            final[1] += i
    
    print(final)

main()