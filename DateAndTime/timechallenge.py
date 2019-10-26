# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

allowed_timezones = [
    "Europe/Minsk",
    "Europe/Monaco",
    "Europe/Moscow",
    "Europe/Nicosia",
    "Europe/Oslo",
    "Europe/Paris",
    "Europe/Podgorica",
    "Europe/Prague",
    "Europe/Riga",
    "Europe/Rome"
]

while True:
    print(allowed_timezones)
    timezone = input("Please select a timezone from the list above: ")
    local_time = datetime.datetime.now()
    utc_time = datetime.datetime.utcnow()
    if timezone == "quit":
        break
    elif timezone in allowed_timezones:
        tz_to_display = pytz.timezone(timezone)
        aware_local_time = pytz.utc.localize(utc_time).astimezone()
        aware_utc_time = pytz.utc.localize(utc_time)
        timezone_time = pytz.utc.localize(utc_time).astimezone(tz_to_display)
        print("Aware timezone time is {}, timezone is {}".format(timezone_time, timezone_time.tzinfo))
        print("Aware local time is {}, timezone is {}".format(aware_local_time, aware_local_time.tzinfo))
        print("Aware UTC time is {}, timezone is {}".format(aware_utc_time, aware_utc_time.tzinfo))
    else:
        print("The {} timezone is not allowed".format(timezone))
