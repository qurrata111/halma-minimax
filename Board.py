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

    def get_board(self):
        return self.board
    
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

    def set_pieces(self, size):
        for i in range (0, size):
            # merah
            for j in range (0, size-i):
                self.set_piece_at(self.RED, i, j)
            # hijau
            curRow = (size*2) - (size - i)
            startCol = size*2 - 1 - i
            endCol = size * 2
            for col in range (startCol, endCol):
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
    
    def get_winner(self):
        greenWin = False
        redWin = False

        # cek jika semua pemain green sudah berada di sisi merah
        for pos in self.greenSide:
            if self.get_piece_at(pos[0], pos[1]) == False or self.get_piece_at(pos[0], pos[1]) == 2:
                redWin = False
                break
            elif self.get_piece_at(pos[0], pos[1]) == 1:
                redWin = True
        for pos in self.redSide:
            if self.get_piece_at(pos[0], pos[1]) == False or self.get_piece_at(pos[0], pos[1]) == 1:
                greenWin = False
                break
            elif self.get_piece_at(pos[0], pos[1]) == 2:
                greenWin = True
        winner = (redWin, greenWin)
        
        return winner

    def print_board(self):
        for i in range (0, self.get_height()):
            if i==0:
                print("  ", i, end="  ")
            elif i==self.get_height()-1:
                print(i)
            else:
                print(i, end="  ")
        count = 0
        for row in self.board:
            print(count, end=" ")
            print(row)
            count +=1
        print()

    def set_board(self, new_board):
        self.board = new_board.copy()

    def is_empty_cell(self, position):
        return (self.get_piece_at(position[0],position[1]) == 0)
    
    def is_valid_move(self, start_pos, end_pos):
        if self.is_empty_cell(end_pos):
            return True
        else:
            return False