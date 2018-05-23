from words import encode, lettersAreNormal, Words
from utils import *


class State:
    @staticmethod
    def ChangeLetters(letter, count):
        return (ord(letter) - ord('а')) * 10 + count
    
    @staticmethod
    def Decode(num):
        return num // 10, num % 10
    
    SuccessfulTurn = 0
    PassTurn = -1
    LettersChange = -2


class Player:
    def __init__(self, words, board):
        self.words = words
        self.board = board

    def lettersAreNormal(self):
        return lettersAreNormal(self.letters)

    @property
    def letters(self):
        return self._letters

    def removeLetters(self, word):
        for i in word:
            try:
                self.letters.remove(i)
            except ValueError:
                self.letters.remove(Words.EMPTY)
        return word

    @property(letters.setter)
    def letters(self, val):
        self._letters = val
        self.pattern, self.empties = encode(self._letters)

    def match(self, pattern):
        temp = str(self.pattern)
        res = 0
        while pattern != 0:
            t = temp % 10
            w = pattern % 10
            w -= t
            if w > 0:
                res += w
            temp //= 10
            pattern //= 10
        res -= self.empties
        if res < 0:
            res = 0
        return res

    @virtual
    def turn(self):
        return State.PassTurn

    @virtual
    def turn0(self):
        return State.PassTurn