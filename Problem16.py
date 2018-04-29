# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:08:17 2018

@author: George

Project Euler problem 15 https://projecteuler.net/problem=15

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""
power = 1000
number = 2**power
totSum = 0

for i in str(number):
    totSum += int(i)

print("The sum of all digits in 2^{} is {}".format(power, totSum))
