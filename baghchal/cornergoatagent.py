from agent import Agent
from game import Game
from const import Const
from move import Move
import random

class cornergotagent(Agent):
    def __init__(self,game : Game, side : int):
        super(CornerGoatAgent, self).__init__(game, side)
        if side != Const.MARK_GOAT:
            raise ValueError("Side must be goat")

    def propse(self) -> Move:
        game : Game = self.game
        board : List[List[int]] = game.board
        moves = self.game.goatMoves
        if(board[0][0] == Const.MARK_NONE):
            return move
        elif(board[0][4] == Const.MARK_NONE):
            return move 
        elif(board[4][0] == Const.MARK_NONE):
            return move 
        elif(board[4][4] == Const.MARK_NONE):
            return move 
        else:
            return random.choice(moves)

   # def isCornerOpen(self, row : int, col : int):
     #   game : Game = self.game
      #  board : List[List[int]] = game.board 
