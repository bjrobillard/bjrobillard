#! /usr/bin/env python3

#---------------------------------
# Project: Project 2: Kattis Prob: Buka (https://open.kattis.com/problems/buka)
# Author: Benjamin Robillard
# Date Created: 10-06-22
#---------------------------------


from dataclasses import dataclass
import sys
 
def answer(firNum, op, secNum):
    if (op == "+"):
        return(firNum + secNum)
    elif (op == "*"):
        return(firNum * secNum)

def solve():
    firstNum = int(input())
    operand = input()
    secondNum = int(input())
    print(answer(firstNum,operand,secondNum))

    # data=sys.stdin.readlines() #alot quicker than reading line by line by line
    # temps = list(map(int, data[1].split()))
    # for line in data:


def test():
    assert answer(10, '*', 10), 10000
    assert answer(100, '+', 100), 200
    print("All test cases passed... ")

# if __name__ == "__main__":
#     if len(sys.argv) > 1 and sys.argv[1] == 'test':
#         test()
#     else:
#         solve()

if __name__ == "__main__":
    solve()