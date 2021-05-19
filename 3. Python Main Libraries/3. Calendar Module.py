import calendar

year = 1976
month = 2
day = 14

# A single month calendar
print(calendar.month(year, month))

# A full year calendar: year, date column width, number of lines per week,
# number of spaces between months column, number of columns
print("The calender of year 2018 is : ")
print(calendar.calendar(2021, 3, 1, 6))

for name in calendar.month_name:
    print(name)

for name in calendar.day_name:
    print(name)

print(calendar.isleap(2016))
print(calendar.weekday(1976, 2, 14))
print(calendar.weekheader(1))
print(calendar.weekheader(2))
print(calendar.weekheader(3))
