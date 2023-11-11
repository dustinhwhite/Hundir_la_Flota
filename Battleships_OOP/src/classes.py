# Aquí es donde definirías tu clase Tablero. 
# Esta clase manejará la lógica del tablero del juego, inicializándolo, colocando barcos, manejando disparos, etc.

import random 
import numpy as np
import variables


BOAT_SIZES = {1: 4, 2: 3, 3: 2, 4: 1}  # Clave = Tamaño del barco, Valor = Cantidad de barcos

class Board:
    def __init__(self, size=variables.SIZE, boat_symbol=variables.BOAT, boat_sizes=BOAT_SIZES):
        self.size = size
        self.boat_symbol = boat_symbol
        self.boat_sizes = boat_sizes
        self.board = np.full((size, size), "O" , dtype='<U4')
        self.boats_placed = {key: 0 for key in boat_sizes} # Contador de boats in boat sizes, cada valor empieza con cero

    
    def is_space_free (self, row, col, boat_size, is_horizontal):
        if is_horizontal: 
            if col + boat_size > self.size:
                return False
            return np.all(self.board[row, col: col + boat_size] == "O") # Check if the horizontal space is free
        else:
            if row + boat_size > self.size:
                return False
            return np.all(self.board[row: row + boat_size, col] == "O") # Check if the vertical space is free


    def place_boat(self, row, col, boat_size, is_horizontal): 
        if is_horizontal: 
            for i in range(boat_size):
                self.board[row, col + i] = self.boat_symbol
        else: 
            for i in range(boat_size):
                self.board[row + i, col] = self.boat_symbol 


    def place_all_boats(self):
        for boat_size in self.boat_sizes:   # Go through each boat size defined in BOAT_SIZES
            required_boats_count = self.boat_sizes[boat_size]   # Get the number of boats of this size we need to place

            while self.boats_placed[boat_size] < required_boats_count:  # Keep placing boats until we have placed the required #
                is_horizontal = random.choice([True, False])    # Generates is_horizontal variable random choice
                row = np.random.randint(0, self.size)   # Generate a random starting position for the boat
                col = np.random.randint(0, self.size)

                if is_horizontal:   
                    col = np.random.randint(0, self.size - boat_size + 1)
                else:
                    row = np.random.randint(0, self.size - boat_size + 1)
            
                if self.is_space_free (row, col, boat_size, is_horizontal): # Check if the boat can be placed at the starting position
                    self.place_boat(row, col, boat_size, is_horizontal) # If it can, place the boat on the board
                    self.boats_placed[boat_size] += 1   # Increase the count of boats placed for this size


    def display_board(self):
        print(self.board)

    
    

# Ejemplos del uso:
# board_game = Board()
# board_game.place_all_boats()
# board_game.display_board()


# ENEMY BOARD and TRACKING BOARD, 4 EN TOTAL 



# class Game:
#     def __init__(self):
#         # Crear tableros para jugador:
#         self.player_board = Board()
#         self.player_tracking_board = Board()

#         # Crear tableros para maquina:
#         self.computer_board = Board()
#         self.computer_tracking_board = Board()

#         # Llenar tablero con barcos:
#         self.player_board.place_all_boats()
#         self.computer_board.place_all_boats()

#     def play(self):
#         # Gameplay va aquí como SHOOT/DISPARO y TERMINAR cuando acabe 20 disparos aciertos 
#         

    # Mas metodos de gameplay aquí


# Game initalized:Ask the user for their name
user_name = input("Please enter your name: ")

# Greet the user
print(f"Welcome to the game, {user_name}!")

print("El objetivo del juego es hundir todos los barcos de tu oponente antes de que la maquina hunda los tuyos.\n")

print("Para jugar, introduce las coordenadas de la casilla donde quieres lanzar un misil.\n\n"
    " - Si aciertas en una casilla donde hay un barco, lo dañarás y se marcará en tu tablero. \n"
    " - Si fallas, se marcará en tu tablero y será el turno de tu oponente.\n")



 
Jugador=pd.DataFrame(board_own)
Maquina=pd.DataFrame(board_blank) 
espacio=pd.DataFrame(np.full((10,1),"|"))
resultado=pd.concat([Jugador,espacio,Maquina],axis=1)   # Va a imprimir los dos tableros lado a lado con un seperador  
print(resultado)       