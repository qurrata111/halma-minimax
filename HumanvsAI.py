from Board import Board
from Node import Node
from AIPlayer import AIPlayer

class HumanvsAI:
    def __init__(self, bsize, tlimit, option):
        self.p1 = option
        if (option == 1):
            self.p2 = 2
        else:
            self.p2 = 1

        self.machine = AIPlayer(tlimit, 5)
        # create board
        self.board_game = Board(bsize)
        self.bsize = bsize

    def start(self):
        # isi pieces ke board
        self.board_game.set_pieces(int(self.bsize/2))
        self.board_game.print_board()
        winner = self.board_game.get_winner()
        while (winner[0] == False or winner[1] == False):
            # input pemain 1
            print("Giliran Anda!")
            print("Masukkan piece target yang akan dipindah!")
            x1 = int(input("X: "))
            y1 = int(input("Y: "))
            while (self.board_game.get_piece_at(x1, y1) == 0 or self.board_game.get_piece_at(x1, y1) != self.p1):
                print("Koordinat yang dipilih tidak valid!")
                print("Masukkan kembali piece yang akan dipindah!")
                x1 = int(input("X: "))
                y1 = int(input("Y: "))
            start_pos = (x1, y1)
            print("Masukkan lokasi piece yang akan dipindah")
            x2 = int(input("X: "))
            y2 = int(input("Y: "))
            end_pos = (x2, y2)
            while not(self.board_game.is_valid_move(start_pos, end_pos)):
                print("Koordinat yang dituju tidak valid!")
                print("Masukkan kembali lokasi piece yang akan dipindah")
                x2 = int(input("X: "))
                y2 = int(input("Y: "))
            end_pos = (x2, y2)
            self.board_game.move_piece(start_pos,end_pos)
            print(self.board_game.turn)
            print("board setelah Human memilih moves")
            self.board_game.print_board()
            # giliran AI yang pindah
            root_node = Node(self.p1, self.board_game, 3) # buat node
            _, best_moves= self.machine.alphaBeta_minimax(root_node)
            print("Giliran AI!")
            print("board setelah AI memilih moves")
            print("best moves", best_moves)
            self.board_game.print_board()
        # get the winner
        winner = self.board_game.get_winner()
        if winner[0] == True and winner[1] == False:
            print("RED player win!")
        if winner[0] == False and winner[1] == True:
            print("RED player win!")
        if winner[0] == True and winner[1] == True:
            print("Game tied!")