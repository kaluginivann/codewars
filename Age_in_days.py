# Did you ever want to know how many days old are you? Complete the function which returns your age in days. The birthdate is given in the following order: year, month, day. You can assume it is in the past.

# For example if today is 30 November 2015 then

# 2015, 11, 1 => "You are 29 days old"
# Suggestions on how to improve the kata are welcome!

from datetime import date

def age_in_days(year, month, day):
    birthdate = date(year, month, day)
    today = date.today()
    days_old = (today - birthdate).days
    return f'You are {days_old} days old'