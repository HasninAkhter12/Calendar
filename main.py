# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = 2034  # year
mm = 12    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))