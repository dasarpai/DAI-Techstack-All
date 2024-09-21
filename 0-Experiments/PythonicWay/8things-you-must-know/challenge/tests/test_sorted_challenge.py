from sorted_challenge import get_sorted, Country

def test_sorted():
    expected = [
                Country('jordan', '10000000iso'), 
                Country('Portugal', '10000000iso'), 
                Country('netherlands', '17500000iso'), 
                Country('niger', '24000000iso'), 
                Country('Taiwan', '24000000iso'), 
                Country('nepal', '30000000iso'), 
                Country('japan', '128000000iso'), 
                Country('nigeria', '198000000iso')
                ]
    actual = get_sorted()
    assert actual == expected
    