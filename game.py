from player import State
from board import Board
from bag import Bag

# usage: game = Game(CompPlayer(), UserPlayer())


class Game:
    scores = {}  # TODO: fill or init

    def __init__(self, bag = None, board = None, *players):
        if not players:
            players = CompPlayer(), UserPlayer()
        if bag is None:
            bag = Bag()
        if board is None:
            board = Board()
        self.bag = bag
        self.players = players
        self.board = board
        self._index = 0
        self._fails = 0

    def run(self):
        while not self.bag and any(not i.letters for i in self.players):
            self.currentPlayer.turn()
            self.nextPlayer()

    def nextPlayer(self):
        self._index += 1
        self._index = val % len(self.players)

    @property
    def currentPlayer(self):
        return self.players[self._index]

    def removeLetters(self, letters):
       self.bag.add(
            self.currentPlayer
                .removeLetters(letters)
        )
        
    def swapLetters(self):
        self.currentPlayer.letters = self.bag.get(self.bag.add(self.letters))
    
    def _normal_turn(self):
        self.currentPlayer.turn()

    def _turn(self)
        self.currentPlayer.turn0()
    
    def swapTurn(self):
        self._turn = self._normal_turn
        self.swapTurn = lambda x: pass

    def turn(self):
        self.currentPlayer.letters += self.bag.get(
            7 - len(self.currentPlayer.letters)
        )
        state = self._turn()
        if state > 0:
            letter, count = State.Decode(state)
            self.removeLetters(letter * count)
            return True
        elif state == State.LettersChange:
            self.swapLetters()
            self.fail()
        elif state == State.SuccessfulTurn:
            self._fails = 0
            self.swapTurn()
        else: # State = Pass Turn
            self.fail()
        self.nextPlayer()

    def fail(self):
        self._fails += 1
        if self._fails >= len(self.players):
            counts = [self.bag.add(i.letters) for i in self.players]
            for i, j in zip(self.players, counts):
                i.letters = self.bag.get(j)
            self._fails = 0
