from datetime import date, timedelta, datetime

# A couple who have been married for 65 years were both
# born on August 16, seven years apart. The man is 2555 days
# older than his wife. In what years were they born?

# lets make an assumption that the wife was at least 16 when she was married,
# so the husband must have been 23, so a starting point for his birth year is:
# this year - 65 - 23

start_year = datetime.now() - timedelta(days=(65 + 23) * 365)
year = start_year.year

found = False
while not found:
    husband = date(year, 8, 16)
    wife = husband + timedelta(days=2555)
    if wife.day == 16:
        if husband.month == wife.month:
            print('Husband born in {0} and wife in {1}'.format(husband.year, wife.year))
            found = True
    year -= 1
