import time
import math
from Node import Node
from Board import Board

class EnginePlayer:
    def __init__(self, timeLimit, alphaBeta):
        self.move_list = []
        self.selected_piece = 0
        self.selected_post = ()
        self.previous_spot = []
        self.limit_time = timeLimit
        self.start = 0
        self.end = 0
        self.prune = 0
        self.alphaBeta = alphaBeta
        self.board = 0

    def generate_move(self, board, player):
        pass

    def hop_search(self, row, col, board):
        pass

    def generate_legal_moves(self, row, col, board):
        pass

    def utility(self, node):
        pass

    def clear_move_list(self):
        self.move_list = []

    def distance(self, p1, p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

    def alphaBeta_minimax(self, node):
        pass

    def max_value (self, node, alpha, beta):
        pass

    def min_value (self, node, alpha, beta):
        pass
    