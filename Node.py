class Node:
    def __init__(self, player, board, nodeDepth):
        self.board = board
        self.player = player
        self.nodeDepth = nodeDepth
        self.nodeValue = 0
        self.children = []
        self.move = 0
        self.to_explore = True

    def get_board(self):
        return self.board

    def get_player(self):
        return self.player

    def get_value(self):
        return self.nodeValue

    def get_depth(self):
        return self.nodeDepth

    def get_children(self):
        return self.children

    def can_explore(self):
        return self.to_explore
    
    def set_value(self, val):
        self.nodeValue = val