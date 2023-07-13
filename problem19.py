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

class First_of_month_day_calculator(object):
    def __init__(self):
        #  Use the key that day 0 = Monday, day 6 = Sunday.
        self.normal_lens = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.leap_lens = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        print(f"No. of days in a normal year: {np.sum(self.normal_lens)}")
        print(f"No. of days in a leap year: {np.sum(self.leap_lens)}")

    def no_first_sundays(self, start_day=6, leap=False):
        """ Given a start day and whether or not it's a leap year,
        return the number of sundays in that year and the start day
        of the following year"""
        month_lens = self.leap_lens if leap else self.normal_lens
        no_sundays_int = 0
        day = start_day
        for days in month_lens:
            if start_day == 6:
                no_sundays_int += 1
            end_day = (start_day + (days - 1)) % 7
            start_day = (end_day + 1) % 7
        return no_sundays_int, start_day

    @staticmethod
    def is_leap(year):
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        elif year % 4 == 0:
            return True
        else:
            return False



def main():
    calc = First_of_month_day_calculator()
    years = np.linspace(1900, 2000, 101).astype(int)
    tot_no_sundays = 0
    start_day = 0
    for year in years:
        leap = calc.is_leap(year)
        no_sundays, start_day = calc.no_first_sundays(start_day=start_day, leap=leap)
        if year > 1900:
            tot_no_sundays += no_sundays
    print(f"Total number of Sundays on first of months = {tot_no_sundays}")


if __name__ == '__main__':
    main()

