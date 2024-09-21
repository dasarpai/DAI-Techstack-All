from min_max_challenge import letter_scores, get_scrabble_dictionary, score_word, get_word_largest_score

def test_words_uppercase():
    assert score_word('ABANDON') == 10
    assert score_word('VOID') == 8

def test_words_lowercase():
    assert score_word('biodiversity') == 21
    assert score_word('entrepreneurs') == 15

def test_madeup_words():
    assert score_word('sheeps') == 0
    assert score_word('xylophenatic') == 0

def test_word_largest_score():
    assert get_word_largest_score("Beautiful is better than ugly.") == 'Beautiful'
    assert get_word_largest_score("Explicit is better than implicit.") == 'Explicit'

def test_word_with_punctuation():
    assert get_word_largest_score('In the face of ambiguity, refuse the temptation to guess.') == 'ambiguity'
    assert get_word_largest_score('Errors should never pass silently.') == 'silently'

def test_madeup_sentence():
    # All of the words have a score of 0, return the first word
    assert get_word_largest_score('wefpie fefq fqpw pwqww') == 'wefpie'
    assert get_word_largest_score('pwqw zxxz lmpny zsxrwq') == 'pwqw'