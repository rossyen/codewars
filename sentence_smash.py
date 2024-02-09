# sentence_smash.py
'''
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. 
Be careful, there shouldn't be a space at the beginning or the end of the sentence!

'''

def smash(words):
    a = []
    string = str()
    if words == a:
        return ("")
    elif len(words) <= 1:
        return string.join(words)
    elif len(words) > 1:
        string = " ".join(str(element) for element in words)
        return string



def main():
    empty_list = []
    single_item_list = ["hello"]
    multiple_item_list = ["hello", "world"]
    mil2 = ["hello", "amazing", "world"]
    mil3 = ["this", "is", "a", "really", "long", "sentence"]
    #print(smash(empty_list))
    #print(smash(single_item_list))
    #print(smash(multiple_item_list))
    #print(smash(mil2))
    #print(smash(mil3))


if __name__ == "__main__":
    main()
