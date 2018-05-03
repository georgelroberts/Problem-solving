# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:29:34 2018

@author: George

Project Euler problem 18 https://projecteuler.net/problem=18

Find the largest summed route from top to bottom of a triange of numbers.

It makes sense to start from the bottom and work my way up. For example, start
at the 14th (penultimate) row and calculate the maximum sum of each number with
the two underneath it. This new array is the new 14th row. Repeat this process
until the top is reached, which will give the maximum path sum.
"""

import pandas as pd

triangle = pd.read_csv('Data\Project18Data.txt', header=None)


def maxUnderArray(array1, array2):
    """Takes 2 arrays, when len(array1) = len(array2)-1, and returns a new
    array of length len(array1) that is the maximum sum of each element in
    array1 with the 2 elements underneath it in array2."""

    newArray = []

    for el in range(len(array1)):
        newArray.append(max(array1[el] + array2[el],
                            array1[el] + array2[el + 1]))

    return newArray


# Array 1 is on top of array 2. To start, calculate the max sum of row 14 with
# row 15. This is then the new row 14. Do the same with row 13 and the new row
# 14.
array2 = list(map(int, triangle.iloc[triangle.size-1][0].split()))
for row in reversed(range(triangle.size-1)):  # Just add the top row at the end
    array1 = list(map(int, triangle.iloc[row][0].split()))
    array2 = maxUnderArray(array1, array2)

maxNo = array2[0]
