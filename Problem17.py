# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:14:04 2018

@author: George

Project Euler problem 17 https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.

"""

# Manually write the number of letters in the spoken words roots

noLetters = {1: "one",
             2: "two",
             3: "three",
             4: "four",
             5: "five",
             6: "six",
             7: "seven",
             8: "eight",
             9: "nine",
             10: "ten",
             11: "evelen",
             12: "twelve",
             13: "thirteen",
             14: "fourteen",
             15: "fifteen",
             16: "sixteen",
             17: "seventeen",
             18: "eighteen",
             19: "nineteen",
             20: "twenty",
             30: "thirty",
             40: "forty",
             50: "fifty",
             60: "sixty",
             70: "seventy",
             80: "eighty",
             90: "ninety",
             100: "onehundred",
             200: "twohundred",
             300: "threehundred",
             400: "fourhundred",
             500: "fivehundred",
             600: "sixhundred",
             700: "sevenhundred",
             800: "eighthundred",
             900: "ninehundred",
             1000: "onethousand"}  # 100s also have an 'and' if with a number


def noLettersInNumber(n, noLetters):
    baseWords = list(noLetters.keys())
    baseWords.sort(reverse=True)  # Sort high to low
    totNoLetters = 0
    for base in baseWords:
        if n == 0:
            break
        elif n - base < 0:  # Check if the number contains a root word
            continue
        else:
            if n % 100 != 0 and n != 1000 and n > 100:
                # This adds the case where an 'and' is needed
                totNoLetters += 3
            n -= base
            totNoLetters += len(noLetters[base])

    return totNoLetters


totNoLetters = sum(noLettersInNumber(i, noLetters) for i in range(1, 1001))
print(f"The number of all letters between 1 and 1000 is {totNoLetters}")
