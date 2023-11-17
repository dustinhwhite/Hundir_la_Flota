# Funciones no incluidas en las Clases
import numpy as np
from src.variables import *

def initial_board():
    '''
    Function that initializes a "water" board without boats.
    
    Returns: Numpy array 
    '''
    init_board = np.full((variables.SIZE,variables.SIZE), variables.WATER)
    return init_board

# AÑADIR EXCEPCIONES DE LOS INPUT !!
def get_guess(): 

    """Prompts the user for a row and column to attack. The
    return value is a board position in (row, column) format.
    """
    c = input("Introduzca una columna(A-J):  o escribe 'salir' para salir del juego): ").upper()
    col = row_column_names[c] # Letters to numbers
    row = int(input("Enter a row (1-10): "))
    
    if get_guess.upperr() == "SALIR":
        print("Thank you for playing!. ¡Hasta la próxima!")
    return (row-1, col-1) 


def check_guess(player_tracking_board, computer_board, position): #input dos tableros
    """Checks whether or not position is occupied by a ship. A hit is
    registered when position occupied by a ship and position not hit
    previously. A miss occurs otherwise.
    param position: a (row,column) tuple guessed by user
    return: guess_status: True when guess results in hit, False when guess results 
    """
    row, col = position
    if (player_tracking_board[row][col] == variables.BOAT_DAMAGED) or (player_tracking_board[row][col] == variables.MISS):
        print("Ya has disparado a esas coordenadas, vuelve a intentarlo")
        return False
    else:
        if computer_board[row][col] == variables.WATER:
            print("Missed!")
            player_tracking_board[row][col] = variables.MISS
            return False
        else:
            print("Hit!")
            player_tracking_board[row][col] = variables.BOAT_DAMAGED
            return True

def end_game(board):
    cont = np.count_nonzero(board == variables.BOAT_DAMAGED)
    return cont
