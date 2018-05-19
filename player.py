from words import encode

class Player:
    # pattern, empties = encode(...)
    def __init__(self, letters = None):
        self.pattern, self.empties = encode(letters)
    
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
        if res < 0: res = 0
        return res