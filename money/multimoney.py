
class Money(object):
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def equals(self, other):
        return (type(self) is type(other)) and (self.amount == other.amount)

    __eq__ = equals

    def __ne__(self, other):
        return not (self == other)

    def __mul__(self, multiplier):
        return self.times(multiplier)

    __rmul__ = __mul__

class Dollar(Money):
    '''represents Uncle Sam's currency'''

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

class Franc(Money):
    '''represents the currency of the Gnomes of Switzerland'''

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
