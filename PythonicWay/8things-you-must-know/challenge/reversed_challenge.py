import re

def remove_punctuation(words):
    '''Helper function to return a string, removing all punctuations and spaces'''
    return re.sub('\W+', '', words)

def is_palindrome(words):
    '''Palindromes are case insensitive, so both radar and Radar are valid'''
    pass # Replace this line with your solution