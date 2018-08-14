from .array_shift import insert_shift_array

def test_element_gets_added_even():
    expected = [2,4,5,6,8]
    actual = insert_shift_array([2,4,6,8], 5)
    assert expected == actual

def test_element_gets_added_odd():
    expected = [4,8,15,16,23,42]
    actual = insert_shift_array([4,8,15,23,42], 16)
    assert expected == actual

def test_element_gets_added_small():
    expected = [4, 16, 8]
    actual = insert_shift_array([4,8], 16)
    assert expected == actual

def test_element_gets_added_small_odd():
    expected = [4, 8, 16, 77]
    actual = insert_shift_array([4, 8, 77], 16)
    assert expected == actual