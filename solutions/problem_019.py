from datetime import date, timedelta

START_DATE = date(1901, 1, 1)
END_DATE = date(2000, 12, 31)
LIMIT = END_DATE - START_DATE
SUNDAY = 6

first_sundays = 0

for i in range(LIMIT.days + 1):
    d = START_DATE + timedelta(days=i)

    if d.day == 1 and d.weekday() == SUNDAY:
        first_sundays += 1


print(first_sundays)
