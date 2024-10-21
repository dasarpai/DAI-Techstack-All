from anyall_challenge import contains_punctuation

def test_with_punctuation():
    assert contains_punctuation('Readability counts.') 
    assert contains_punctuation('If the implementation is hard to explain, it\'s a bad idea.')
    assert contains_punctuation('There should be one-- and preferably only one --obvious way to do it.')

def test_no_punctuation():
    assert contains_punctuation('Errors should never pass silently') == False
    assert contains_punctuation('Simple is better than complex') == False
