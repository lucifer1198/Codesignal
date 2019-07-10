"""
Given some time output the time after one second.

Example

For currentTime = [23, 59, 59], the output should be
nextSecond(currentTime) = [0, 0, 0].
"""


def nextSecond(currentTime):
    hour = currentTime[0]
    minute = currentTime[1]
    second = currentTime[2]

    second += 1
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        hour += 1
    if hour == 24:
        hour = 0
    return [hour, minute, second]
