from tablero import Board
import random 

class Game:
    def __init__(self):
        # Crear tableros para jugador:
        self.player_board = Board()
        self.player_tracking_board = Board()

        # Crear tableros para maquina:
        self.computer_board = Board()
        self.computer_tracking_board = Board()

        # Llenar tablero con barcos:
        self.player_board.populate_board()
        self.computer_board.populate_board()

    def play(self):
        # Game play va aquí
        pass

    # Mas metodos de gameplay aquí

