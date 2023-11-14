# Funciones no incluidas en las Clases

import numpy as np
import variables

def initial_board():
    '''
    Función que inicializa un tablero "agua" de unas determinadas dimensiones 
        Input:
        Output:
    '''
    init_board = np.full((variables.SIZE,variables.SIZE), "~")
    return init_board


def display_boards(player_board, player_tracking_board):

    '''
    Función que imprime por pantalla de una forma visual el tablero de barcos del jugador y su tablero de disparos.
        Input:
        Output:
    '''

    column_names = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
    print()
    
    # Titles
    left_title = "YOUR BOATS"
    right_title = "YOUR SHOOTS"

    # Print titles
    print(' ' * 9 + left_title, end="")
    print('  ' * 11 + right_title)


    # Print column names (left board)
    print('     ', end='')  # Space to align columns names
    for letter in column_names.keys():
        print('{:^2}'.format(letter), end='')

    # Print column names (right board)
    print(' '*13, end='')  # # Space to align columns names
    for letter in column_names.keys():
        print('{:^2}'.format(letter), end='')

    print()

    # Print boards
    for row in range(variables.SIZE):
        # Print left board
        print('{:2} |'.format(row + 1), end=' ')
        print(*player_board[row], end=" ")
        print('|', end=' ')

        # Space between both boards
        print(' '*5  , end=' ')

        # Print right board
        print('{:2} |'.format(row + 1), end=' ')
        print(*player_tracking_board[row], end=" ")
        print('|')
    
    print()