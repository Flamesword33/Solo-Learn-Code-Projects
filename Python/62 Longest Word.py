"""Longest Word.py
Given a text sample as an input, find and output the longest word.
"""

def main(txt:str):
    text_list = txt.split(' ')

    longest = 0
    counter = 0
    desired_word = 0

    for word in text_list:
        word = remove_punctuation(word)
        if len(word) > longest:
            longest = len(word)
            desired_word = counter
        counter += 1
    
    return text_list[desired_word]

def remove_punctuation(txt:str):
    pass

out = main("Hello my baby, Hello my honey, hello my rag time gall, you set my heart on fire, truely my one desire!")
print(out)