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

def positionInWord(letter, word):
    return (i for i in range(len(word)) if word[i] == letter)

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

    WEIGHTS = {
        'а': 1, 'б': 3, 'в': 1, 'г': 3, 'д': 2, 'е': 1, 'ж': 5, 'з': 5, 'и': 1,
        'й': 5, 'к': 1, 'л': 2, 'м': 2, 'н': 1, 'о': 1, 'п': 2, 'р': 1, 'с': 1,
        'т': 1, 'у': 2, 'ф': 10, 'х': 5, 'ц': 5, 'ч': 5, 'ш': 8, 'щ': 10,
        'ъ': 12, 'ы': 5, 'э': 8, 'ю': 8, 'я': 4, 'ь': 3, 'ё': 0
    }
    ADIITIONAL_WEIGHT = 6

    def scores(_, st):
        val = 0
        for i in st:
            val += self.WEIGHTS[i]
        if len(st) > 4:
            val += self.ADDITIONAL_WEIGHT * (len(st) - 4)
        return val

    def getMatches(self, x):
        return word for word, pattern in self.words.all
            if self.match(pattern) == x

# TODO: search
