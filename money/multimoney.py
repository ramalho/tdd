
class Money(object):
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def __rmul__(self, multiplier):
        return self * multiplier

    def __eq__(self, other):
        return (type(self) is type(other)) and (self.amount == other.amount)

    def __ne__(self, other):
        return not (self == other)


class Dollar(Money):
    '''represents Uncle Sam's currency'''

    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier)

class Franc(Money):
    '''represents the currency of the Gnomes of Switzerland'''

    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier)
