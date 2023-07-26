#!/usr/bin/env python
# coding: utf-8

# In[1]:


import difflib
import nltk

nltk.download('words')
from nltk.corpus import words

class AutoCorrect:
    def __init__(self, word_list):
        self.word_list = word_list

    def correct_word(self, word):
        word = word.lower()
        closest_word = difflib.get_close_matches(word, self.word_list, n=1)
        if closest_word:
            return closest_word[0]
        else:
            return "No suggestion found."

# Load the standard English word list from nltk
word_list = set(words.words())

# Initialize the AutoCorrect object with the word list
auto_correct = AutoCorrect(word_list)

# Take user input for the word to be corrected
user_input = input("Enter a word to be corrected: ")

# Correct the word
corrected_word = auto_correct.correct_word(user_input)

print(f"Original word: {user_input}")
print(f"Corrected word: {corrected_word}")


# In[ ]:




