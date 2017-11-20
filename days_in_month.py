"""
This program is part of my coursera project that will be graded.
"""
import datetime

def days_in_month(year, month):
    """
    This function computes the number of days in a month.
    Inputs:
      year - an integer between datetime.MINYEAR and datetime.MAXYEAR
             representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """

    #sanity checking that the input year is valid
    # if (datetime.MINYEAR <= year <= datetime.MAXYEAR):
    #     print("The year: " + str(year) + " is between the valid MIN and MAX year.")
    # else:
    #     print("The year: " + str(year) + " is not between the valid MIN and MAX year.")

    next_month = month + 1
    if next_month == 13:
        next_month = 1
        next_year = year + 1

    date1 = datetime.date(year, month, 1)
    date2 = datetime.date(next_year, next_month, 1)

    difference = date2 - date1

    print("Number of days is: " + str(difference.days))


days_in_month(2017,12)
