from player import Player
from words import Words

class CompPlayer(Player):
    def turn0(self):
        while not self.lettersAreNormal and Words.EMPTY not in self.letters:
            self.swapLetters()
        try:
            word = min(
                word for word, pattern in self.word.all
                    if self.match(pattern) < 0,
                key = lambda x: return Words.scores(x)
            )
            column = self.board.findBestInCenter(word)
            self.board.place(word, self.board.centerVertical, column)
            self.removeLetters(word)
            return True
        except ValueError:
            return False
