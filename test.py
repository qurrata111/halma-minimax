from Board import Board
from Node import Node
from AIPlayer import AIPlayer

p1 = 1 # red
p2 = 2 # green
machine2 = AIPlayer(10,2) #ai
# create board
board_game = Board(8)
board_game.print_board()
print()
# isi pieces ke boarsd
board_game.set_pieces(4)
board_game.print_board()
# input pemain 1
print("Masukkan piece target yang akan dipindah!")
x1 = int(input("X: "))
y1 = int(input("Y: "))
print("Masukkan lokasi piece yang akan dipindah")
x2 = int(input("X: "))
y2 = int(input("Y: "))
start_pos = (x1, y1)
end_pos = (x2, y2)
board_game.move_piece(start_pos,end_pos)
print(board_game.turn)
print("board setelah Human memilih moves")
board_game.print_board()
# giliran AI yang pindah
root_node = Node(2, board_game, 3) # buat node
_, best_moves = machine2.alphaBeta_minimax(root_node)
print("board setelah AI memilih moves")
print("best moves", best_moves)
board_game.print_board()