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
    #print("Next month = " + str(next_month))
    #print("Date 1 = " + str(date1))

    if next_month == 1:
        year = year + 1
    date2 = datetime.date(year, next_month, 1)
    #print("Date 2 = " + str(date2))

    difference = date2 - date1
    #print("Value of 'difference' variable is: " + str(difference))
    rt_diff = difference.days
    print("Number of days in the input month is: " + str(rt_diff))
    return rt_diff



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


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1   - an integer representing the year of the first date
      month1  - an integer representing the month of the first date
      day1    - an integer representing the day of the first date
      year2   - an integer representing the year of the second date
      month2  - an integer representing the month of the second date
      day2    - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is before
      the first date.
    """
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    if (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2) and date1 <= date2 ) == True:
        difference = date2 - date1
        rt_diff = difference.days
        print("Days between the first and second dates = " + str(rt_diff))
        return rt_diff
    else:
        #print("First condition failed! Returning 0.")
        return 0


def age_in_days(year, month, day):
    """
    Inputs:
      year   - an integer representing the birthday year
      month  - an integer representing the birthday month
      day    - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input date
      is in the future.
    """

    birthday = datetime.date(year, month, day)
    current_day = datetime.datetime.now().date()
    if (is_valid_date(year, month, day) and (birthday < current_day)):
        difference = current_day - birthday
        rt_diff = difference.days
        print("My age in days is: " + str(rt_diff) + " days")
        return rt_diff

    else:
        #print("Return 0 because my input date is invalid or the input date is in the future!")
        return 0


age_in_days(1977, 12, 28)
days_between(2017, 12, 31, 2018, 1, 2)
is_valid_date(2017, 12, 31)
days_in_month(2017, 2)