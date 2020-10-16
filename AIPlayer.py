import time
import math
from Node import Node
from Board import Board

class AIPlayer:
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
        self.boards = 0

    def jump_search(self, row, col, board):
        offsets = [-1,0,1]
        jumps = []
        game_board = Board(len(board))
        for row_offset in offsets:
            for col_offset in offsets:
                if (row+row_offset) >= len(board) or (col+col_offset >= len(board)):
                    continue
                if (row+row_offset) < 0 or (col+col_offset) < 0:
                    continue
                if (row+row_offset) == row and (col+col_offset) == col:
                    continue

                if (board[row+row_offset][col+col_offset] != 0):
                    row_jump_offset = row + 2*row_offset
                    col_jump_offset = col + 2*col_offset

                    if (row_jump_offset >= len(board)) or (col_jump_offset >= len(board)):
                        continue
                    if (row_jump_offset < 0) or (col_jump_offset < 0):
                        continue

                    if (board[row+2*row_offset][col+2*col_offset] == 0) and ((row+2*row_offset, col+2*col_offset) not in self.previous_spot):
                        if (board[row][col] == 1 and (row, col) not in game_board.redSide):
                            if ((row_jump_offset, col_jump_offset) in game_board.redSide):
                                continue
                        if (board[row][col] == 2 and (row, col) not in game_board.greenSide):
                            if ((row_jump_offset, col_jump_offset) in game_board.greenSide):
                                continue
                        self.previous_spot.append((row, col))
                        jumps.append((row+2*row_offset, col+2*col_offset))
                        further_hops = self.jump_search(row_jump_offset, col_jump_offset, board)
                        jumps.extend(further_hops)
                        self.move_list.extend(further_hops)
        return jumps

    def generate_valid_moves(self, row, col, board):
        # mengenerate perpindahan yg legal dari posisi row,col
        game_board = Board(len(board))
        if row >= len(board) or col >= len(board):
            print("Position is out of bounds!")
            return
        if row < 0 or col < 0:
            print("Position is out of bounds!")
            return
        if board[row][col] == 0:
            print("Nothing to be moved!")
            return

        offsets = [-1,0,1]
        valid_moves = []
        blocked_spaces = []

        for row_offset in offsets:
            for col_offset in offsets:
                if (row+row_offset) >= len(board) or (col+col_offset >= len(board)):
                    continue
                if (row+row_offset) == row and (col+col_offset) == col:
                    continue
                if (row+row_offset) < 0 or (col+col_offset) < 0:
                    continue

                if (board[row+row_offset][col+col_offset] == 0):
                    if (board[row][col] == 1) and (row, col) not in game_board.redSide:
                        if ((row+row_offset, col+col_offset) in game_board.redSide):
                            continue
                    if (board[row][col] == 2) and (row, col) not in game_board.greenSide:
                        if ((row+row_offset, col+col_offset) in game_board.greenSide):
                            continue
                    valid_moves.append((row+row_offset, col+col_offset))
                else:
                    blocked_spaces.append((row+row_offset, col+col_offset))
        valid_moves.extend(self.jump_search(row, col, board))
        self.move_list.extend(valid_moves)
        return valid_moves
                
    def utility(self, node):
        board = node.board
        data_board = board.get_board()
        cek_win = board.get_winner()
        value = 0
        red = 0
        green = 0

        for col in range (board.get_width()):
            for row in range (board.get_height()):
                # get pemain
                piece = data_board[row][col]
                if piece == 1: # pemain red
                    distance_list = [] # list jarak dari cur pos ke goal pos
                    for goal in board.greenSide: # posisi di goal
                        if data_board[goal[0]][goal[1]] != 1:
                            distance_list.append(self.distance((row, col), goal))
                            red += max(distance_list) if len(distance_list) else -100
                if piece == 2: # pemain green
                    distance_list = [] # list jarak dari cur pos ke goal pos
                    for goal in board.redSide: # posisi di goal
                        if data_board[goal[0]][goal[1]] != 2:
                            distance_list.append(self.distance((row, col), goal))
                            green += max(distance_list) if len(distance_list) else -100
    
        value = red/green if node.player == 1 else green/red
        #value = float("inf") if cek_win[0] else float("inf") # kalau sudah ada yang menang
        if cek_win[0]:
            value = float("inf")
        elif cek_win[1]:
            value = float("inf")

        return value

    def clear_move_list(self):
        self.move_list = []

    def distance(self, p1, p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

    def alphaBeta_minimax(self, node):
        self.start = time.time()
        node_max, best_move = self.max_value(node, float("-inf"), float("inf"))
        data_board = node.get_board()
        print("best move", best_move)
        data_board.move_piece(best_move[0], best_move[1])
        print("Waktu yg dibutuhkan :", self.end-self.start, "detik untuk berpindah.")
        print("Pruning             :", self.prune, "cabang.")
        print("Generated           :", self.boards, "board.")
        # clear
        self.prune = 0
        self.boards = 0
        data_board.chosenMove = best_move
        data_board.changeTurn()
        return node_max, best_move

    def max_value (self, node, alpha, beta):
        print("Get maximum value from node...")
        self.end = time.time()
        board = node.get_board()
        
        cek_win = board.get_winner()
        best_move = None
        
        if (cek_win[0] == True or cek_win[1] == True or node.get_depth() <= 0 or self.end-self.start > self.limit_time):
            val = self.utility(node)
            node.set_value(val)
            return node, best_move
        player = node.get_player()
        
        if player == 1:
            player_pos = board.get_green_position()
        elif player == 2:
            player_pos = board.get_red_position()
        
        value = float("-inf")
        data_board = board.get_board()
        for move in player_pos:
            valid_moves = self.generate_valid_moves(move[0], move[1], data_board)
            if len(valid_moves) == 0:
                continue
            for valid_move in valid_moves:
                self.end = time.time()
                if (self.end-self.start > self.limit_time):
                    return node,best_move
                self.boards += 1
                board_copy = Board(node.get_board().get_height())
                board_copy.set_board(data_board)
                board_copy.move_piece(move, valid_move)
                next_node = Node(player, board_copy, node.get_depth()-1)
                next_node.move = (move, valid_move)

                child_node, _ = self.min_value(next_node, alpha, beta)
                board_copy.move_piece(valid_move, move)
                if value < child_node.get_value():
                    move_from = move
                    move_to = valid_move
                    best_move = (move_from, move_to)
                value = max(value, child_node.get_value())

                return_node = next_node
                if value > beta and self.alphaBeta:
                    self.prune += 1
                    return_node.set_value(beta)
                    return return_node, None
                
                alpha = max(alpha, value)
        
        return_node.set_value(value)
        return return_node, best_move

    def min_value (self, node, alpha, beta):
        print("Get minimum value from node...")
        self.end = time.time()
        board = node.get_board()
        cek_win = board.get_winner()
        best_move = None 
        if (cek_win[0] == True or cek_win[1] == True or node.get_depth() <= 0 or self.end-self.start > self.limit_time):
            val = self.utility(node)
            node.set_value(val)
            return node, best_move

        player = node.get_player()

        if player == 1:
            player_pos = board.get_green_position()
        elif player == 2:
            player_pos = board.get_red_position()
        
        vals = float("inf")
        data_board = board.get_board()
        for move in player_pos:
            valid_moves = self.generate_valid_moves(move[0], move[1], data_board)
            if (len(valid_moves) == 0):
                continue
            for valid_move in valid_moves:
                self.end = time.time()
                if (self.end-self.start > self.limit_time):
                    return node,best_move
                self.boards += 1
                board_copy = Board(node.get_board().get_height())
                board_copy.set_board(data_board)
                board_copy.move_piece(move, valid_move)
                next_node = Node(player, board_copy, node.get_depth()-1)
                next_node.move = (move, valid_move)

                child_node, _ = self.max_value(next_node, alpha, beta)
                board_copy.move_piece(valid_move, move)
                if vals > child_node.get_value():
                    move_from = move
                    move_to = valid_move
                    best_move = (move_from, move_to)
                vals = min(vals, child_node.get_value())
                return_node = next_node
                if vals < alpha and self.alphaBeta:
                    self.prune += 1
                    return_node.set_value(vals)
                    return return_node, None
                
                beta = min(beta, vals)
        
        return_node.set_value(vals)
        return return_node, best_move