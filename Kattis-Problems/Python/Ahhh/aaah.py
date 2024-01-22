#! /usr/bin/env python3

import sys

def solution(pati, doc):
    if (len(doc) > len(pati)):
        return "no"
    else:
        return "go"
    

def kattis():
    patient = input()
    doctor = input()

    print(solution(patient, doctor))

if __name__ == "__main__":
    kattis()