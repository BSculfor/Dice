from random import seed
from random import randint
seed(a=None)

class dice(object):
    def __init__(self, sides):
        self.sides=sides

    def roll(self):
        return randint(1, self.sides)

d6 = dice(6)
d6.roll()
        



        
