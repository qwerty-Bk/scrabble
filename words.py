from collections import Counter

def encode(word):
    res = 0
    empties = 0
    word = word.lowercase()
    for letter in word:
        if letter == 'ё':
            empties += 1
        else:
            res += 10 ** (ord(l) - ord('а'))
    return res, empties


vowels = tuple('уеыаоэяию')
def lettersAreNormal(letters):
    if len(letters) < 7:
        return True
    cntr = Counter(letters)
    vow = 0
    for i, j in cntr.items():
        if i in vowels:
            vow += j
        if j > 2 or vow > 5:
            return False
    return vow >= 2

class Words:
    EMPTY = 'ё'
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

# TODO: search
