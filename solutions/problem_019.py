from datetime import date, timedelta

SUNDAY = 6

def solve(start_date, end_date):
    first_sundays = 0
    limit = end_date - start_date

    for i in range(limit.days + 1):
        d = start_date + timedelta(days=i)

        if d.day == 1 and d.weekday() == SUNDAY:
            first_sundays += 1

    return first_sundays


if __name__ == "__main__":
    print(solve(date(1901, 1, 1), date(2000, 12, 31)))
