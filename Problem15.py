# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:40:55 2018

@author: George

Project Euler problem 15 https://projecteuler.net/problem=15

Find the number of unique routes for unit vectors across a 20x20 square.

The number of routes to each element, N(i,j) can be calculated as N(i,j-1) +
N(i-1,j)
"""

import numpy as np


def numRoutes(rows, cols):
    """ Calculates the number of routes in an ixj array"""

    routeArray = np.zeros((rows+1, cols+1))

    # There is only one way to each outside edge piece
    routeArray[0, :] = 1
    routeArray[:, 0] = 1
    for row in range(rows):
        for col in range(cols):
            routeArray[row+1, col+1] = routeArray[row+1, col] + routeArray[row, col+1]

    return int(routeArray[rows, cols])

print(numRoutes(20, 20))

# Also note that this problem is a lot easier using combinations. We know that
# at the end there will have been i right movements and j down movements, we
# just need to know where they go. This is simply (i+j) choose i.