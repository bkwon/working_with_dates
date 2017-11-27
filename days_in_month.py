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
        year = year + 1

    date1 = datetime.date(year, month, 1)
    print("Next month = " + str(next_month))
    print("Date 1 = " + str(date1))

    if next_month == 1:
        year = year + 1
    date2 = datetime.date(year, next_month, 1)
    print("Date 2 = " + str(date2))

    difference = date2 - date1
    rt_diff = difference.days
    print("Number of days is: " + str(rt_diff))
    return rt_diff


days_in_month(2017, 2)


def is_valid_date(year,month,day):
    """
    Inputs:
      year  - an integer repersenting the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date
      False otherwise
    """
    max_days = days_in_month(year, month)
    #print("Max_Days = " + str(max_days))
    #date = datetime.date(year, month, day)

    if ((datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1 <= month <= 12) and (1 <= day <= max_days)):
        #print("The date: " + str(date) + " is valid.")
        date_valid = True
        print(date_valid)
        return date_valid
    else:
        #print("The year: " + str(date) + " is not valid.")
        date_valid = False
        print(date_valid)
        return date_valid


is_valid_date(2017, 12, 31)


