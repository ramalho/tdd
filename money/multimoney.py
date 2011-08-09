class Dollar(object):
    '''represents Uncle Sam's currency'''
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier

    def __imul__(self, multiplier):
        self.times(multiplier)
        return self