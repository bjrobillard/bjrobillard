#! /usr/bin/env python3
import sys

def solution(lines):
    maxNum = -1000000
    for i in lines[1:len(lines)]:
        # print("I: ", i)
        if int(maxNum) <= int(i):
            maxNum = i
        else:
            maxNum = maxNum


    minNum = 1000000
    for i in lines[1:len(lines)]:
        # print("I: ", i)
        if int(minNum) >= int(i):
            minNum = i
        else:
            minNum = minNum
    rangeNum = int(maxNum) - int(minNum)

    return str(minNum) + " " + str(maxNum) + " " + str(rangeNum)
        

def kattis():
    inpt = []
    for line in sys.stdin.readlines():
        inpt.append(line.split())
        # print("line", line)
        
        
    # print(inpt)
    counter = 1
    for line in range(0, len(inpt)):
        print("Case " + str(counter) + ":", solution(inpt[line]))
        counter += 1


if __name__ == "__main__":
    kattis()