from Board import Board
from Node import Node
from AIPlayer import AIPlayer
from AIPlayer2 import AIPlayer2

class AIvsAI:
    def __init__(self, bsize, tlimit, option):
        self.p1 = option
        if (option == 1):
            self.p2 = 2
        else:
            self.p2 = 1
        self.machine1 = AIPlayer(tlimit, 5)
        # self.machine2 = AIPlayer(tlimit, 5)
        self.machine2 = AIPlayer2(tlimit)
        # create board
        self.board_game = Board(bsize)
        self.bsize = bsize
        
    def start(self):
        # isi pieces ke board
        self.board_game.set_pieces(int(self.bsize/2))
        self.board_game.print_board()
        winner = self.board_game.get_winner()
        # inisiasi yg pindah
        start_pos = (1,2)
        end_pos = (2,3)
        # self.board_game.move_piece(start_pos, end_pos)
        while (self.board_game.get_winner() == (False, False)):
            # giliran AI1 pindah
            root_node1 = Node(self.p2, self.board_game, 2) # buat node
            _, best_moves1 = self.machine1.alphaBeta_minimax(root_node1)
            print("Giliran AI1 + alpha beta pruning!")
            print("board setelah AI1 memilih moves")
            print("best moves", best_moves1)
            self.board_game.print_board()
            print()
            print()
            # giliran AI2 yang pindah
            root_node2 = Node(self.p1, self.board_game, 2) # buat node
            _, best_moves2 = self.machine2.localSearch_minimax(root_node2)
            print("Giliran AI2 + local search!")
            print("board setelah AI2 memilih moves")
            print("best moves", best_moves2)
            self.board_game.print_board()
            print()
            print()
            
        # get the winner
        winner = self.board_game.get_winner()
        if winner[0] == True and winner[1] == False:
            print("RED player win!")
        if winner[0] == False and winner[1] == True:
            print("GREEN player win!")
        if winner[0] == True and winner[1] == True:
            print("Game tied!")
        print("Total waktu yang dibutuhkan alpha beta minimax", self.machine1.total_time, "detik.")
        print("Total waktu yang dibutuhkan minimax + local search", self.machine2.total_time, "detik.")
