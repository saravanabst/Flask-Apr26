from square import get_square
def test_positive():
    x=5
    expected=25
    res = get_square(x)
    assert res==expected

def test_one():
    x=1
    expected=1
    res = get_square(x)
    assert res==expected

def test_negative():
    x=-5
    expected=25
    res = get_square(x)
    assert res==expected
