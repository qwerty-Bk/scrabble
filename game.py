from player import CompPlayer, UserPlayer
from board import Board
from bag import Bag

# usage: game = Game(CompPlayer(), UserPlayer())

class Game:
    scores = {} # TODO: fill or init

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
    
    def __normal_turn(self):
        if self.currentPlayer.turn(): self.fails = 0
        else: self.fail()
        self.nextPlayer()

    def fail(self):
        self._fails += 1
        if self._fails >= len(self.players):
            counts = [self.bag.add(i.letters)) for i in self.players]
            for i, j in zip(self.players, counts):
                i.letters = self.bag.get(j)
            self._fails = 0
     
    def turn(self):
        if self.currentPlayer.turn0():
            self.turn = self.__normal_turn
            self._fails = 0
        else:
            self.fail()
 