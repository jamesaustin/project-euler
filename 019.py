# 1 Jan 1900 was a Monday.
#
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
#
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

import datetime

m = 0
for x in xrange(1901, 2001):
    for y in xrange(1, 13):
        if datetime.date(x, y, 1).weekday() == 6:
            m += 1
print m

# or

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m = 0
d = 1
for x in xrange(1901, 2001):
    for y in xrange(0, 12):
        if x % 4 == 0:
            d += leap[y]
        else:
            d += months[y]
        if d % 7 == 6:
            m += 1
print m