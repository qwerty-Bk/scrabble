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

# TODO: search
