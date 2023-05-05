import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(f"{day_of_week}-{month}-{year}")

date_of_birth = dt.datetime(year=2000, month=10, day=25, hour=5, minute=43)
print(date_of_birth)
