# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 18:56:53 2018

@author: George

Project Euler problem 11 https://projecteuler.net/problem=11

With a 20-20 grid, find the maximum product of four adjacent numbers (up, down,
diagonal, anti-diagonal)

This solution works quickly, with no overlaps between products, and is
functionalised for understanding
"""

import numpy as np

os.chdir('C:\\Users\\George\\OneDrive - University Of Cambridge\\Others\\Project Euler')

array = np.genfromtxt('Data\\Project11Data.txt')


def vertProd(array, index):
    """ Input is an n-dimensional array, and a tuple representing the desired
    index. Output is the product of the four elements to the right """

    subArray = array[index[0]:index[0] + 4, index[1]]
    prod = np.prod(subArray)

    return prod


def horProd(array, index):
    """ The same as above, but horizontal products """

    subArray = array[index[0], index[1]:index[1] + 4]
    prod = np.prod(subArray)

    return prod


def diagProdsMax(array, index):
    """ The same as the above functions, but diagonal and antidiag products """

    subArray = array[index[0]:index[0] + 4,
                     index[1]:index[1] + 4]
    subArrayDiag = np.diag(subArray)
    subProd = np.prod(subArrayDiag)
    subArrayAntiDiag = np.diag(np.fliplr(subArray))
    subAntiDiagProd = np.prod(subArrayAntiDiag)

    maxProd = max([subProd, subAntiDiagProd])

    return maxProd


def maxSurroundingProducts(array, index):
    """ Finds max of all of the above """
    return max([vertProd(array, index),
                horProd(array, index),
                diagProdsMax(array, index)])


maxProd = 0
for i in range(17):
    for j in range(17):
        currentProd = maxSurroundingProducts(array, (i, j))
        if currentProd > maxProd:
            maxProd = currentProd
            print(maxProd)

print("The final maximum product is {}".format(int(maxProd)))