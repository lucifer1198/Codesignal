# 187 chars
def getMonthName(mo):
    months = {
        1: "Jan", 2: "Feb", 3: "Mar", 4:"Apr", 
        5: "May", 6: "Jun", 7: "Jul", 8:"Aug", 
        9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
    }
    if mo in months.keys():
        return months.get(mo)
    return "invalid month"

# 124 chars
def getMonthName(m):
    d = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
    for k, v in enumerate(d):
        if m == k+1:
            return v
    return "invalid month"

# 72 chars
import calendar as c
getMonthName = lambda m:  c.month_abbr[m%13] or "invalid month"

# 67 chars
import imaplib as c
getMonthName = lambda m:c.Months[m%13] or 'invalid month'

'''
>>> getMonthName(1)
"Jan"
>>> getMonthName(0)
"invalid month"
>>>
'''
