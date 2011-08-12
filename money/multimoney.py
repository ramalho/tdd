class Dollar(object):
    '''represents Uncle Sam's currency'''
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __mul__(self, multiplier):
        return self.times(multiplier)

    __rmul__ = __mul__

    def equals(self, other):
        return self.amount == other.amount

    __eq__ = equals

    def __ne__(self, other):
        return self.amount != other.amount

class Franc(object):
    '''represents Uncle Sam's currency'''
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def __mul__(self, multiplier):
        return self.times(multiplier)

    __rmul__ = __mul__

    def equals(self, other):
        return self.amount == other.amount

    __eq__ = equals

    def __ne__(self, other):
        return self.amount != other.amount
