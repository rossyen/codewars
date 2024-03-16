# isograms.py

'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
'''

test = "moOse"
def is_isogram(string):
    alpabeth = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    for letter in alpabeth:
        if string.count(letter) >= 2:
            return False
    return True


print(is_isogram(test))


#best practice from codewars:
'''
def is_isogram(string):
    return len(string) == len(set(string.lower()))
'''
