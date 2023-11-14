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
        self.board = np.full((size, size), "~" , dtype='<U4')
        self.boats_placed = {key: 0 for key in boat_sizes} # Contador de boats in boat sizes, cada valor empieza con cero

    
    def is_space_free (self, row, col, boat_size, is_horizontal):
        if is_horizontal: 
            if col + boat_size > self.size:
                return False
            return np.all(self.board[row, col: col + boat_size] == "~") # Check if the horizontal space is free
        else:
            if row + boat_size > self.size:
                return False
            return np.all(self.board[row: row + boat_size, col] == "~") # Check if the vertical space is free


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
    #test123


