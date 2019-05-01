"""
Author: G. L. Roberts
Date: 1st May 2019

About: You are given the following information, but you may prefer to
       do some research for yourself.
        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4, but not
            on a century unless it is divisible by 400.
        How many Sundays fell on the first of the month during the
            twentieth century (1 Jan 1901 to 31 Dec 2000)?

Approach: There are 14 different scenarios, based on the first day of
            the year. Calculate the number of Sundays in a year for
            each day it can start with, both with and without a leap
            year.

"""

import numpy as np

def main():
    #  Use the key that day 0 = Monday, day 6 = Sunday.
    normal_month_lens = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_month_lens = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print("No. of days in a normal year: {}".format(np.sum(normal_month_lens)))
    print("No. of days in a leap year: {}".format(np.sum(leap_month_lens)))


if __name__ == '__main__':
    main()

