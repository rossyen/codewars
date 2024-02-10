# count_positive_sum_negatives.py

'''
DESCRIPTION:
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

'''

# attempt at code with some help form chatGPT after i got error on [] should equal [0,0]
def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return []
    positive_sum = 0
    negative_sum = 0
    for num in arr:
        if num > 0:
            positive_sum += 1
        elif num < 0:
            negative_sum += num

    return [positive_sum, negative_sum]

# best practice from codewars
'''
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]
'''