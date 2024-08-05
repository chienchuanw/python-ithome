# 1. Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime

now = datetime.now()
day, month, year, hour, minute, timestamp = (
    now.day,
    now.month,
    now.year,
    now.hour,
    now.minute,
    now.timestamp(),
)
print(
    f"day: {day}, year: {year}, hour: {hour}, minute: {minute}, timestamp: {timestamp}"
)


# 2. Format the current date using this format: `"%m/%d/%Y, %H:%M:%S"`

from datetime import datetime

current_date = datetime.now()
print(current_date.strftime("%m/%d/%Y, %H:%M:%S"))

# 3. Today is 5 December, 2019. Change this time string to time.

from datetime import datetime

today = "5 December, 2019"
print(datetime.strptime(today, "%d %B, %Y"))

# 4. Calculate the time difference between now and new year.

from datetime import datetime, date

now = datetime.now()
new_year = date(year=2025, month=1, day=1)

diff = new_year - now.date()
print(diff)


# 5. Calculate the time difference between 1 January 1970 and now.

from datetime import date, datetime

now = datetime.now()
new_year = date(year=1970, month=1, day=1)

diff = now.date() - new_year
print(diff)


# 6. Think, what can you use the datetime module for?
#    Examples:
#    - Time series analysis
#    - To get a timestamp of any activities in an application
#    - Adding posts on a blog
