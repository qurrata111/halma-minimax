class Board:
    RED = 1 # PLAYER
    GREEN = 2 # PLAYER
    EMPTY = 0 # EMPTY PIECE

    def __init__(self, size):
        # informasi Board
        self.board = []
        self.size = size
        self.greenSide = []
        self.redSide = []
        self.turn = 2

        # inisiasi empty space
        for i in range (0, size):
            row = []
            for j in range (0, size):
                row.append(self.EMPTY)
            self.board.append(row)

        self.set_red_corner(int(size/2))
        self.set_green_corner(int(size/2))
        self.chosenMove = 0
    
    def get_height(self):
        return self.size

    def get_width(self):
        return self.size
    
    def get_green_position(self):
        greenPosition = []
        for i in range (0, self.get_height()):
            for j in range (0, self.get_width()):
                if (self.board[i][j] == self.GREEN):
                    greenPosition.append((i,j))
        return greenPosition

    def get_red_position(self):
        redPosition = []
        for i in range (0, self.get_height()):
            for j in range (0, self.get_width()):
                if (self.board[i][j] == self.RED):
                    redPosition.append((i,j))
        return redPosition

    def set_red_corner(self, size):
        for i in range (0, size):
            for j in range (0, size-i):
                self.redSide.append((i,j))
    
    def set_green_corner(self, size):
        # di bawah
        for i in range (0, size):
            curRow = (size * 2)  - (size - i)
            startCol = size * 2 - 1 - i
            endCol = size * 2
            for col in range (startCol, endCol):
                self.greenSide.append((curRow, col))

    def init_piece(self, size):
        for i in range (0, size):
            # merah
            for j in range (0, size-i):
                self.set_piece_at(self.RED, i, j)
            # hijau
            curRow = (size*2) - (size - i)
            startCol = size*2 - 1 - i
            endCol = size * 2
            for col in range (startCol, endCol):
                print(curRow, col)
                self.set_piece_at(self.GREEN, curRow, col)

    def get_piece_at(self, row, col):
        return self.board[row][col]
    
    def set_piece_at(self, player, row, col):
        self.board[row][col] = player

    def remove_piece_at(self, row, col):
        # get original pemain
        player = self.board[row][col]
        # hapus
        self.board[row][col] = self.EMPTY
        return player
    
    def move_piece(self, start_pos, end_pos):
        player = self.remove_piece_at(start_pos[0], start_pos[1])
        self.set_piece_at(player, end_pos[0], end_pos[1])
    
    def changeTurn(self):
        # mengubah giliran
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1
    
    def getTheWinner(self):
        greenWin = False
        redWin = False

        # cek jika semua pemain green sudah berada di sisi merah
        for pos in self.greenSide:
            if self.get_piece_at(pos[0], pos[1]) == False:
                redWin = False
                break
            elif self.get_piece_at(pos[0], pos[1]) == True:
                redWin = True
        for pos in self.redSide:
            if self.get_piece_at(pos[0], pos[1]) == False:
                greenWin = False
                break
            elif self.get_piece_at(pos[0], pos[1]) == True:
                greenWin = True
        
        return (redWin, greenWin)

    def print_board(self):
        for row in self.board:
            print(row)
        print()
    def set_board(self, new_board):
        self.board = new_board.copy()

b = Board(8)
# awal
print(b.get_green_position())
print(b.get_red_position())
b.print_board()
print()
# inisiasi
b.init_piece(4)
b.print_board()
# after move
b.move_piece((0,3), (0,4))
b.print_board()