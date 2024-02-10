# sum_array_with_exception.py

'''
DESCRIPTION:
Task
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
Input validation
If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.
'''

# first attempt - does not work because if arr is type none it checks if len first and gets error.
'''def sum_array(arr):
    if len(arr) <= 1 or arr == None:
        return 0
    else:
        return sum(arr)-min(arr)-max(arr)'''

# second attempt -> works
def sum_array(arr):
    if arr == None or len(arr) <= 1:
        return 0
    else:
        return sum(arr)-min(arr)-max(arr)
    
# best practice from codewars
'''
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
'''