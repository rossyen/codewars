# grasshopper_grade_book.py

'''
DESCRIPTION:
Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
'''

# first attempt (this is also 2nd attempt. I had wrong return output in first attempt)
# every return was "A" in first attempt.

from calculate_average import find_average

def get_grade(s1, s2, s3):
    average = [s1, s2, s3]
    if 90 <= find_average(average) <= 100:
        return "A"
    elif 80 <= find_average(average) <= 90:
        return "B"
    elif 70 <= find_average(average) <= 80:
        return "C"
    elif 60 <= find_average(average) <= 70:
        return "D"
    elif 0 <= find_average(average) < 60:
        return "F"

    
# best practice from codewars
'''
def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"
'''
