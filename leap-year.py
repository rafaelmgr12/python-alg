
def leap_year(year):
    """Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
    Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

