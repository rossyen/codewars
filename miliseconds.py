# clock.py
'''
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

'''

# first attempt
def time_since_midnight(h, m, s):
    return ((h*60*60*1000)+(m*60*1000)+(s*1000)) if 0 <= h <= 23 and 0 <= m <= 59 and  0 <= s <= 59 else 0

   
# test
print(time_since_midnight(0,1,1))

# best practice from codewars
'''
def past(h, m, s):
    return (3600*h + 60*m + s) * 1000
'''