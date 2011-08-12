from multimoney import Dollar

def test_multiplication():
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount

def test_inplace_multiplication():
    seven = Dollar(7)
    seven *= 3
    assert 21 == seven.amount
