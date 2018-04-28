# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 07:13:04 2018

@author: George

Project Euler problem 11 https://projecteuler.net/problem=14

Find the longest Collatz sequence starting under 1 million

If n is even -> n/2. If n is odd -> 3n + 1

All numbers end at 1. Which starting number under 1 million gives the longest
chain?

# Speed up notes: I have used a default dictionary to store all the previously
encountered sequence lengths, removing unnecessary computations.
"""

from  collections import defaultdict

def nextStep(seqNo):
    """ Finds the next number based on the current number. Returns a tuple with
    the next number, and the number of steps taken"""
    if seqNo % 2 == 0:
        return seqNo // 2
    else:
        return 3 * seqNo + 1


maxCollatzLength = 0
maxCollatzStartNo = 0
lengthDict = defaultdict()

for curNo in range(2, 1000000):
    collatzLength = 1
    startNo = curNo

    while curNo > 1: # The sequence end is reached if curNo=1
        if curNo in lengthDict:
            collatzLength += lengthDict[curNo]
            break
        else:
            curNo = nextStep(curNo) # Manually calculate the next number
            collatzLength += 1

    lengthDict[startNo] = collatzLength

    if collatzLength > maxCollatzLength:
        maxCollatzLength = collatzLength
        maxCollatzStartNo = startNo
