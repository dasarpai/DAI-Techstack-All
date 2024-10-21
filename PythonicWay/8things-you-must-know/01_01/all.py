def valid_rgb(rgb):
    '''Receives (r, g, b)  tuple, 
       Checks if each rgb int is within (0, 255) inclusive'''    
    for val in rgb:
        if not 0 <= val <= 255:
            return False
    return True

assert valid_rgb((25, 5, 225)) == True
assert valid_rgb((255, 255, 255)) == True
assert valid_rgb((290, 100, 200)) == False
assert valid_rgb((250, 300, 200)) == False
assert valid_rgb((250, 100, 400)) == False
print('Passed all tests ...')

