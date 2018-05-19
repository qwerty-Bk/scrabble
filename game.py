from player import CompPlayer
from board import Board

# usage: game = Game(CompPlayer(), UserPlayer())

class Game:
    scores = {} # TODO: fill or init

    def __init__(self, comp = None, user = None):
        if comp is None:
            comp = CompPlayer()
        if user is None:
            user = UserPlayer()
        self.comp = comp
        self.user = user
        self.board = Board()
    
    def __normal_turn(self):
        pass
     
    def turn(self):
        self.turn = self.__normal_turn
        