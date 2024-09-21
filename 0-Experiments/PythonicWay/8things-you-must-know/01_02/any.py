def contains_digit(input_str):
    for char in input_str:
        if char.isdigit():
            return True
    return False

assert contains_digit('This sentence does not contain any digits') == False
assert contains_digit('But th15 0ne d0e5') == True
assert contains_digit('123-456-7890')
print('Passed all tests ...')

