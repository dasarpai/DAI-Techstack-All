from reversed_challenge import is_palindrome, remove_punctuation

def test_palindromes():
    assert is_palindrome('sagas')
    assert is_palindrome('Radar')
    assert is_palindrome('Was it a cat I saw?')
    assert is_palindrome('Eva, can I see bees in a cave?')
    assert is_palindrome('Red rum, sir, is MURDER!!')

def test_non_palindromes():
    assert is_palindrome("This should not not work") == False
    assert is_palindrome('radars') == False