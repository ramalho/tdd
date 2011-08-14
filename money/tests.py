from multimoney import Dollar, Franc

def test_multiplication():
    five = Dollar(5)
    product = five * 2
    assert Dollar(10) == product
    product = 3 * five
    assert Dollar(15) == product

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)
    assert Dollar(5) != Franc(5)

def test_franc_multiplication():
    five = Franc(5)
    product = five * 2
    assert Franc(10) == product
    product = 3 * five
    assert Franc(15) == product
