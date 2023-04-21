# A program to analyze the works of Shakespeare

"""
    This Python function reads a text file, removes punctuation and duplicates, and outputs the first
    and last five words alphabetically, as well as the most frequently used words and their counts.
    
    :param words: A string of words to be counted for occurrences
    :return: The function `occurrences` returns a list of tuples, where each tuple contains a word and
    its count of occurrences in the input string.
    """

import sys
import os
import re
def occurrences(words):
    word_list = words.split()
    count = {}
    for word in word_list:
        if word in count.keys():
            count[word] += 1
        else:
            count[word] = 1

    return count.items()
    
### open/read file, change characters to lower case, remove punctuation, create list by splitting sowrds###
file = open('shakespeare.txt', 'r')
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
text2 = text.replace("'", '')
words = list(text2.split())

### remove duplicate words ###
dictionary = dict.fromkeys(words)
deduplicated_list = list(dictionary)
deduplicated_list.sort()

### first five alphabetical ###
print('Five alphabetically first words: ', deduplicated_list[0:5])

### last five ###
print('Five alphabetically last words: ', deduplicated_list[-5:])

### most used words and count ###

most_used1 = (sorted(occurrences(text2), key=lambda x: x[1], reverse=True))

print("The most used words and how many times they appear", most_used1[0:5])

