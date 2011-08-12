from multimoney import Dollar

def test_multiplication():
    five = Dollar(5)
    product = five.times(2)
    assert Dollar(10) == product
    product = five.times(3)
    assert Dollar(15) == product

def test_multiplication_operator():
    seven = Dollar(7)
    product = seven * 3
    assert Dollar(21) == product
    product = 4 * seven
    assert Dollar(28) == product

def test_multiplication_assignment():
    value = Dollar(7)
    value *= 3
    assert Dollar(21) == value

def test_equality():
    assert Dollar(5).equals(Dollar(5))
    assert not Dollar(5).equals(Dollar(6))

def test_equality_operators():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)

