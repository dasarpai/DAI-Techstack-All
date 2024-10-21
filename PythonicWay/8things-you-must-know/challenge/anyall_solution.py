import string

def contains_punctuation(input_str):
    return any(char in string.punctuation
        for char in input_str
    )

assert contains_punctuation('Readability counts.') == True 
assert contains_punctuation('Errors should never pass silently') == False
assert contains_punctuation('If the implementation is hard to explain, it\'s a bad idea.') == True
assert contains_punctuation('There should be one-- and preferably only one --obvious way to do it.') == True
assert contains_punctuation('Simple is better than complex') == False
print('Passed all tests ...')