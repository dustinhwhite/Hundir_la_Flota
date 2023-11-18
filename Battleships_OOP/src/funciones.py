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


def get_guess(): 

    """Prompts the user for a row and column to attack. The
    return value is a board position in (row, column) format.
    """
    while True:
        #print("Introduzca 'salir' si quiere salir y terminar el juego.")
        column_input = input("Introduzca una columna (A-J):").upper().strip()
        
        if column_input  in row_column_names.keys():
            column = row_column_names[column_input] 
            break
        else:
            print(f"{column_input} no es una columna válida. Introduzca una letra de la A a la J:")

    while True:
        row_input = input("Introduzca una fila (1-10): ")
        row_names = list(map(str, list(range(1, 11))))
        
        if row_input in row_names:
            row_input = int(row_input)
            break
        else:
            print(f"{row_input} no es una fila válida. Introduzca un número entero entre 1 y 10:")

    return (row_input-1, column-1) 


def player_shot(player_tracking_board, computer_board, position): 

    '''
    Checks whether or not position is occupied by a ship in the computer board. 
    A hit is registered when position occupied by a ship and position not hit previously. 
    A miss occurs otherwise.
    Args:
        player_tracking_board (Board Class Object): to check the previus shots
        computer_board (Board Class Object): 
        position (tuple) : A tuple with the user coordinates
    Returns: 
    '''
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

#def computer_shot(player_board, computer_shots):


def end_game(board):
    '''
    Function that checks how many damaged ships there are in a board.
    If damaged boats are the same as the total, the game is over and someone wins
    Args: 
        board (Board Class Object) : The board where the damaged boats are counted

    Returns: False if game is over | True if it isn't over.
    '''
    cont = np.count_nonzero(board == variables.BOAT_DAMAGED)

    if cont == 20:
        return False
    else:
        return True
