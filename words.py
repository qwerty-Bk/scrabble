def encode(word):
    res = 0
    e = 0 # empties
    word = word.lowercase()
    for l in word: # letter
        if l == 'ё':
            e += 1
        else:
            res += 10 ** (ord(l) - ord('а'))
    return res, e

class Player:
    # pattern, empties = encode(...)
    
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

class Words:
    # words = {i: encode(i) for i in ...}
    
    def findCandidates(self, player):
        match0 = []
        match1 = []
        for i in words:
            a = player.match(i)
            if a == 0:
                match0.append(a)
            else if a == 1:
                match1.append(a)
        return match1, match0
    
    def x(self):
        pass #xhx
    
# TODO: search;