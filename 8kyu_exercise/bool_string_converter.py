# bool_string_converter.py
'''
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

'''

# first attempt
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    

    
# best practice from codewars
'''
def bool_to_word(bool):
    return "Yes" if bool else "No"
'''