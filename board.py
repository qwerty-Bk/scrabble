# ВСЕ СЛОВА ГОРИЗОНТАЛЬНЫЕ СЛЕВА НАПРАВО

class Board:
    width = 15
    height = 15

    def __init__(self, width=15, height=15):
        self.width = width
        self.height = height
        self.cells = [
            ['*' for i in range(self.width)]
            for j in range(self.height)
        ]

    def place(self, word, cop, ced):
        for i in range(ced[1] - cop[1])