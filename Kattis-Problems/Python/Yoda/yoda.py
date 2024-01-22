#! /usr/bin/env python3

#---------------------------------
# Project: Project 2: Kattis Prob: Yoda (https://open.kattis.com/problems/yoda)
# Author: Benjamin Robillard
# Date Created: 10-06-22
#---------------------------------

 
def answer(fNum,sNum):

    stringFNum = str(fNum) # take input numbers - change to string
    stringSNum = str(sNum)

    fNumStr = "" # new firstNum string to reverse original input 
    sNumStr = ""

    finalFNum = "" # final result initialization
    finalSNum = ""

    if len(stringFNum) > len(stringSNum):
        for i in range(0, len(stringFNum) - len(stringSNum)): # go through and add zero to end of secondNum if firstNum is longer
            sNumStr+="0"
        fNumStr += stringFNum
        sNumStr += stringSNum
    elif len(stringSNum) > len(stringFNum):
        for i in range(0, len(stringSNum) - len(stringFNum)): # same as above but changing firstNum
            fNumStr+="0"
        fNumStr += stringFNum
        sNumStr += stringSNum
    else:                           # if they're equal in len then just add the elems to end of fNumStr/sNumStr
        fNumStr += stringFNum
        sNumStr += stringSNum
    
    for i in range(0, len(fNumStr)):
        if fNumStr[i] > sNumStr[i]:
            finalFNum += fNumStr[i]
        elif sNumStr[i] > fNumStr[i]:
            finalSNum += sNumStr[i]
        else:
            finalFNum += fNumStr[i]
            finalSNum += sNumStr[i]
    
    retval1 = None
    retval2 = None

    if (len(finalFNum) == 0): # check for YODA in firstNum
        retval1 = "YODA"
    else:
        retval1 = int(finalFNum)
    
    if (len(finalSNum) == 0): # check for YODA in secondNum
        retval2 = "YODA"
    else:
        retval2 = int(finalSNum)

    print(retval1)
    print(retval2)
    return retval1, retval2


def solve():
    firstNum = input()
    secondNum = input()
    answer(firstNum, secondNum)

if __name__ == "__main__":
    solve()
