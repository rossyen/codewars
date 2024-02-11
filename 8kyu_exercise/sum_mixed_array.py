# sum_mixed_array.py

'''
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
'''

# first attempt
def sum_mix(arr):
    int_convert = [int(x) for x in arr]
    return sum(int_convert)

# best practice from codewars
'''
def sum_mix(arr):
    return sum(map(int, arr))
'''