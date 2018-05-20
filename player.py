from words import encode


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

    def turn(self):
        raise NotImplementedError(
            "Player::turn not implemented in {0}".format(
                self.__class__.__name__
            )
        )
        return False

    def turn0(self):
        raise NotImplementedError(
            "Player::turn0 not implemented in {0}".format(
                self.__class__.__name__
            )
        )
        return False
