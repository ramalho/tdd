from multimoney import Dollar

def test_multiplication():
    five = Dollar(5)
    product = five.times(2)
    assert 10 == product.amount
    product = five.times(3)
    assert 15 == product.amount

def test_multiplication_operator():
    seven = Dollar(7)
    product = seven * 3
    assert 21 == product.amount
    product = 4 * seven
    assert 28 == product.amount

def test_multiplication_assignment():
    value = Dollar(7)
    value *= 3
    assert 21 == value.amount
