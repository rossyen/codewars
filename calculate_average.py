# calculate_average.py

'''
DESCRIPTION:
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
'''

# first attempt - receives TypeError: '<' not supported between instances of 'list' and 'int'
'''
def find_average(numbers):
    if numbers == None or numbers < 1:
        return 0
    else:
        return sum(numbers)/len(numbers)
'''
    
# second attempt
def find_average(numbers):
    if numbers == None or len(numbers) < 1:
        return 0
    else:
        return sum(numbers)/len(numbers)
    
# best practice from codewars
'''
def find_average(array):
    return sum(array) / len(array) if array else 0
'''