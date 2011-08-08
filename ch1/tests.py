import unittest

from multimoney import Dollar

class TestMultiMoney(unittest.TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEquals(10, five.amount)

    def test_inplace_multiplication(self):
        seven = Dollar(7)
        seven *= 3
        self.assertEquals(21, seven.amount)

if __name__ == '__main__':
    unittest.main()


