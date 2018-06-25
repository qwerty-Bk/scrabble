# ВСЕ СЛОВА ГОРИЗОНТАЛЬНЫЕ СЛЕВА НАПРАВО


class Board:
    EMPTY = ' '

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
            [self.EMPTY for i in range(self.width)]
            for j in range(self.height)
        ]

    def place(self, word, row, column):
        for i in range(len(word)):
            self.cells[row][column + i] = word[i]

    def tryPlace(self, word, row, column):
        for i in range(len(word)):
            if self.cells[row][column + i] not
                in (self.EMPTY, word[i], Words.EMPTY):
                return False
        return True

    def findPositionGenerator(self, word, missingletters):
        for let, offsets in missingletters.items():
            for row in range(self.cells.height):
                for column in range(self.cells.width):
                    if self.cells[row][column] == let:
                        for offset in offsets:
                            if self.tryPlace(word, row, column - offset):
                                yield row, column - offset

    def findPosition(self, word, missingletters):
        try:
            return max(
                (i, cntscr(word, i[0], i[1])) for i
                    in self.findPositionGenerator(word, missingletters),
                key = lambda x: x[1]
            )
        except ValueError:
            return None, None

    def BestConnectedWord(self, letters):
        #todo letters-> woard
        for i in range(self.height):
            for j in range(self.width - len(woard)):
                match = True
                for n in range(len(woard)):
                    if board[i][j] not in (words.EMPTY, woard[n], self.EMPTY):
                        match = False
                        break
                if match:
                    #todo все connectionsy
                    start = self.board[i].rfind(self.EMPTY, j - 1)
                    end = self.board[i].find(self.EMPTY, j + len(word))
                    conn, connStart = None, None
                    if start == -1:
                        if end != -1:
                            conn, connStart = max(self.words.connections(
                                self.board[i][j:end], len(word)
                            ), ...)
                    else:
                        if end == -1:
                            conn, connStart = max(self.words.connections(
                                self.board[i][start:j + len(word)], j - start
                            ), ...)
                        else:
                            len1 = j - start
                            src = self.board[i][start:end]
                            conn, connStart = max(self.words.connections(
                                src, len1
                            ), ...)
                            conn1, connStart1 = max(self.words.connections(
                                src, len1 + len(word)
                            ), ...)
                            conn, connStart = max([
                                (conn, connStart),
                                (conn1, connStart1)
                            ], ...)
                    if conn is not None:
                        pass
                    yield woard, [i, j], ConWord, posOfC, scoresWC



    def findBestInCenter(self, word):
        return max(
            x for x in range(
                max(0, self.centerHorizontal - len(word)),
                min(self.centerHorizontal, self.width - len(word) - 1) + 1
            ),
            key = lambda x: cntscr(word, self.centerVertical, x)
        )

    def cntscr(self, word, row, column):
        pts = 0
        mult = 1
        for i in range(len(word)):
            mult *= self.wordmod[row][column + i]
            pts += self.letmod[row][column + i] * Game.scores[word[i]]
        return pts * mult
