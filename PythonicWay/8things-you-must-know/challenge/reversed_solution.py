import re

def remove_punctuation(words):
    '''Helper function to return a string, removing all punctuations and spaces'''
    return re.sub('\W+', '', words)

def is_palindrome(words):
    reversed_words = ''.join(reversed(words))
    return remove_punctuation(words.lower()) == remove_punctuation(reversed_words.lower())


