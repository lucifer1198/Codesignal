"""
A new parking lot just opened in your city. Its rates are:

- The first 30 minutes (inclusive) of parking are free;
- From 31 minutes to 2 hours, every 10 minutes costs $1;
- Every 10 minutes over 2 hours costs $2.

Since you are charged for every 10 minutes, you should round the number of minutes spent in the parking lot up to the nearest multiple of 10.
For example, if you've been in the parking lot for 43 minutes, you will pay for 50 minutes.

You are given 2 strings: The time you typically arrive at your usual parking lot, and the time you typically leave it.
Now you want to know how much you'll have to pay at the new parking lot. It's guaranteed that all events take place in one day.

Example

For timeIn = "14:11" and timeOut = "14:39", the output should be
parkingCost(timeIn, timeOut) = 0.

You usually spend 28 minutes in the parking lot, so you won't have to pay anything.

For timeIn = "07:02" and timeOut = "07:42", the output should be
parkingCost(timeIn, timeOut) = 1.

You spend 40 minutes in the parking lot, so you'll need to pay for the first 10 minutes after the free half hour.

For timeIn = "12:20" and timeOut = "14:54", the output should be
parkingCost(timeIn, timeOut) = 17.

You spend 2 hours and 34 minutes in the parking lot, so you'll need to pay $9 for the first 2 hours (there are 90 minutes between 30 minutes and 2 hours, each 10 minutes of which cost $1) and 4 * 2 = $8 for the next 34 minutes, for a total of 8 + 9 = 17.
"""


def parkingCost(timeIn, timeOut):
    diff = (int(timeOut[:2]) * 60 +
            int(timeOut[3:]) -
            int(timeIn[:2]) * 60 -
            int(timeIn[3:]))
    if diff <= 30:
        return 0
    if diff <= 120:
        return (diff - 21) // 10
    return 9 + ((diff - 111) // 10) * 2
