"""
Beginner Series #2 Clock

Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
"""

sec = 1000
min = 60000
hour = 3600000

def past(h, m, s):
    mil_hour = hour * h 
    mil_min = min * m
    mil_sec = sec * s

    milliseconds = mil_hour + mil_min + mil_sec
    return milliseconds