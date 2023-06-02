import calendar

# print(calendar.calendar(2022))

# 0 = segunda , 6 = domingo

# print(calendar.monthrange(2022, 12))


# print(calendar.monthcalendar(2022,12))

for week in calendar.monthcalendar(2022, 3):
    print(week)