# Testing merge Epic_branch_1
import random 
import numpy as np
from tabulate import tabulate

row_column_names = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
SIZE = 10
BOAT1 = 4
BOAT2 = 3
BOAT3 = 2
BOAT4 = 1
WATER = "💧"
BOAT ="🚢"
MISS = "💥"
BOAT_DAMAGED = '💀'

HIT_CHAR= BOAT_DAMAGED
MISS_CHAR= "💧"
BLANK_CHAR= "💥"

BOAT_SIZES = {1: 4, 2: 3, 3: 2, 4: 1}  # Clave = Tamaño del barco, Valor = Cantidad de barcos

class Board:
    def __init__(self, size=SIZE, boat_symbol=BOAT, boat_sizes=BOAT_SIZES):
        self.size = size
        self.boat_symbol = boat_symbol
        self.boat_sizes = boat_sizes
        self.board = np.full((size, size), "💧")
        self.boats_placed = {key: 0 for key in boat_sizes} # Contador de boats in boat sizes, cada valor empieza con cero

    
    def is_space_free (self, row, col, boat_size, is_horizontal):
        if is_horizontal: 
            if col + boat_size > self.size:
                return False
            return np.all(self.board[row, col: col + boat_size] == "💧") # Check if the horizontal space is free
        else:
            if row + boat_size > self.size:
                return False
            return np.all(self.board[row: row + boat_size, col] == "💧") # Check if the vertical space is free


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
        '''
        Function that visually prints the player's ship board and their shooting board on the screen.

        Args: 
            self (Board Class Object) : The board to print in console

        Returns : None
        '''
        print(tabulate(self.board.tolist(),headers=variables.row_column_names.keys(), showindex=variables.row_column_names.keys(),tablefmt="rounded_grid",stralign='center'))

# FUNCIONES
def initial_board():
    '''
    Función que inicializa un tablero "agua" de unas determinadas dimensiones 
    
        Input:
        Output:
    '''
    init_board = np.full((SIZE,SIZE), "💧")
    return init_board

def get_guess(): # no self 

    """Prompts the user for a row and column to attack. The
    return value is a board position in (row, column) format.
    """
    c = input("Enter a col (A-J): ").upper()
    col = row_column_names[c] 
    row = int(input("Enter a row (0-9): "))

    # AÑADIR EXCEPCIONES DE LOS INPUT !!

    return (row-1, col-1) #Col, row intercambiado


def check_guess(player_tracking_board, computer_board, position): #input dos tableros
    """Checks whether or not position is occupied by a ship. A hit is
    registered when position occupied by a ship and position not hit
    previously. A miss occurs otherwise.
    param position: a (row,column) tuple guessed by user
    return: guess_status: True when guess results in hit, False when guess results 
    """
    row, col = position
    if (player_tracking_board[row][col] == HIT_CHAR) or (player_tracking_board[row][col] == BLANK_CHAR):
        print("Ya has disparado a esas coordenadas, vuelve a intentarlo")
        return False
    else:
        if computer_board[row][col] == MISS_CHAR:
            print("Missed!")
            player_tracking_board[row][col] = BLANK_CHAR
            return False
        else:
            print("Hit!")
            player_tracking_board[row][col] = HIT_CHAR
            #computer_board[row][col] = HIT_CHAR
            return True

player_board = Board()
player_board.place_all_boats()
tracking_board = initial_board()

'''tabla1 = tabulate(player_board.board.tolist(),headers=variables.row_column_names.keys(), showindex=variables.row_column_names.values(),tablefmt="rounded_grid",stralign='center')
tabla2 = tabulate(tracking_board.tolist(),headers=variables.row_column_names.keys(), showindex=variables.row_column_names.values(),tablefmt="rounded_grid",stralign='center')
'''
while True:
    position = get_guess()

    check_guess(tracking_board, player_board.board, position)

    tabla1 = tabulate(player_board.board.tolist(),headers=row_column_names.keys(), showindex=row_column_names.values(),tablefmt="rounded_grid",stralign='center')
    tabla2 = tabulate(tracking_board.tolist(),headers=row_column_names.keys(), showindex=row_column_names.values(),tablefmt="rounded_grid",stralign='center')

    print(tabla1)
    print(tabla2)

