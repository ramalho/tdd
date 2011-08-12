from multimoney import Dollar

def test_multiplication():
    five = Dollar(5)
    product = five.times(2)
    assert 10 == product.amount
    product = five.times(3)
    assert 15 == product.amount

def test_multiplication_assignment():
    seven = Dollar(7)
    seven *= 3
    assert 21 == seven.amount

'''
public void testMultiplication() {
   Dollar five= new Dollar(5);
   Dollar product= five.times(2);
   assertEquals(10, product.amount);
   product= five.times(3);
   assertEquals(15, product.amount);
}
'''
