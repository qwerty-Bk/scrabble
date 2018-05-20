# ВСЕ СЛОВА ГОРИЗОНТАЛЬНЫЕ СЛЕВА НАПРАВО


class Board:
    def __init__(self, width = 15, height = 15):
        self.width = width
        self.height = height
        self.wordmod = [
            [1 for i in range(self.width)]
            for j in range(self.height)
        ]
        self.letmod = [
            [1 for i in range(self.width)]
            for j in range(self.height)
        ]
        self.cells = [
            ['*' for i in range(self.width)]
            for j in range(self.height)
        ]

    def place(self, word, row, column):
        for i in range(len(word)):
            self.cells[row][column + i] = word[i]

    def cntscr(self, word, row, column):
        pts = 0
        mult = 1
        for i in range(len(word)):
            mult *= self.wordmod[row][column + i]
            pts += self.letmod[row][column + i] * Game.scores[word[i]]
        return pts * mult
