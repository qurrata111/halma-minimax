from HumanvsAI import HumanvsAI
from AIvsAI import AIvsAI

class Menu:
    def __init(self):
        self.bsize = 8
        self.tlimit = 10
        self.player = 1 # red
        self.option = 1
        

    def inisiasi(self):
        print("Permainan Halma")
        print("Jenis permainan!")
        print("1. Human vs AI")
        print("2. AI vs AI")
        print("Board size available 8, 10, 16")
        print("Pemain RED = 1, pemain GREEN = 2")
        print()
        self.option = int(input("Masukkan jenis permainan: "))
        self.bsize = int(input("Masukkan board size     : "))
        self.tlimit = int(input("Masukkan time limit     : "))
        if self.option == 1:
            self.player = int(input("Pilih pemain 1 atau 2   : "))
        if self.get_option() == 1:
            hvsa = HumanvsAI(self.get_bsize(), self.get_tlimit(), self.get_option())
            hvsa.start()
        else:
            ava = AIvsAI(self.get_bsize(), self.get_tlimit(), self.get_option())
            ava.start()
    
    def get_bsize(self):
        return self.bsize
    
    def get_tlimit(self):
        return self.tlimit
    
    def get_pemain_by_user(self):
        return self.player

    def get_option(self):
        return self.option
