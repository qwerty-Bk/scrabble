from words import encode
from utils import *


class Player:
    # pattern, empties = encode(...)
    def __init__(self, letters):
        self.letters = letters

    @property
    def letters(self):
        return self._letters

    @property(letters.setter)
    def letters(self, val):
        self._letters = val
        self.pattern, self.empties = encode(self._letters)

    def match(self, word):
        temp = str(self.pattern)
        res = 0
        while word != 0:
            t = temp % 10
            w = temp % 10
            w -= t
            if w > 0:
                res += w
            temp //= 10
            word //= 10
        res -= self.empties
        if res < 0:
            res = 0
        return res

    @virtual
    def turn(self):
        return False

    @virtual
    def turn0(self):
        return False