#  The year you would like to check if was a leap year.
my_year = 1656


#  Function that checks if year given is a leap year based on given requirements.
def is_leap_year(year):
    if year % 4000 == 0:
        return False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True


#  if statement that prints text to terminal based on whether the year is a leap year or not.
if is_leap_year(my_year):
    print(f"The year {my_year} is a leap year!")
else:
    print(f"The year {my_year} is not a leap year!")


is_leap_year(my_year)


# Attempting commit with github actions
