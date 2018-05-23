from player import Player
from words import Words
from utils import *
from collections import defaultdict


class CompPlayer(Player):
    ATTEMPTS = 5

    def turn0(self):
        while not self.lettersAreNormal and self.words.EMPTY not in self.letters:
            self.swapLetters()
        try:
            word = min(
                self.words.getMatches(0),
                key = lambda x: return self.words.scores(x)
            )
            column = self.board.findBestInCenter(word)
            self.board.place(word, self.board.centerVertical, column)
            self.removeLetters(word)
            return True
        except ValueError:
            return False

    def missingLetters(self, word):
        a = defaultdict(list)
        for i in range(len(word)):
            if word[i] not in self.letters:
                a[word[i]].append(i)
        return a

    def wordsGenerator(self):
        c = 0
        for word in sorted(
            self.words.getMatches(1),
            reversed = True,
            key = lambda x: self.words.scores(x)):
            if c >= self.ATTEMPTS: break
            pos, scores = self.board.findPosition(word, self.missingletters)
            if pos is None: continue
            c += 1
            yield word, pos, scores

    def turn(self):
        c = 0
        while c < self.ATTEMPTS and not self.lettersAreNormal and
            self.words.EMPTY not in self.letters:
            self.swapLetters()
            c += 1
        match0 = self.words.getMatches(0)
        try:
            word, pos, scores = max(self.wordsGenerator(), key = lambda x: x[2])
        except ValueError:
            pass # TODO:
