# Funciones no incluidas en las Clases
import numpy as np
import src.variables as variables
import time

def initial_board():
    '''
    Function that initializes a "water" board without boats.
    
    Returns: Numpy array 
    '''
    init_board = np.full((variables.SIZE,variables.SIZE), variables.WATER)
    return init_board


def get_guess(player_tracking_board): 

    """Prompts the user for a row and column to attack. The
    return value is a board position in (row, column) format.
    """
    while True:
        #print("Introduzca 'salir' si quiere salir y terminar el juego.")
        column_input = input("[ Si quiere abandonar el juego, introduzca 'W' ]\n Introduzca una columna (A-J):").upper().strip()
        if column_input == "W":
            return (99,99)
        else:
            if column_input  in variables.row_column_names.keys():
                column = variables.row_column_names[column_input] 
            else:
                print(f"{column_input} no es una columna válida. Introduzca una letra de la A a la J:")
                continue

            row_input = input("Introduzca una fila (1-10): ")
            row_names = list(map(str, list(range(1, 11))))

   # while True:
            if row_input in row_names:
                row_input = int(row_input)
            else:
                print(f"{row_input} no es una fila válida. Introduzca un número entero entre 1 y 10:")
                continue

            if player_tracking_board[row_input-1, column-1] in [variables.MISS, variables.BOAT_DAMAGED]:
                print("Ya has disparado a esas coordenadas, vuelve a intentarlo")
            else:
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

computer_shots = set()
def computer_shot(player_board, computer_shots):
    '''
    Checks whether or not position is occupied by a ship in the player board. 
    A hit is registered when position occupied by a ship and position not hit previously. 
    A miss occurs otherwise.
    Args:
        player_board (Board Class Object): to check the previus shots
        computer_shots (set) : A set with the computer shots 
    Returns: 
    '''
    
    while True:
        time.sleep(1)
        row = np.random.randint(0, 10)
        col = np.random.randint(0, 10)
        
        if (row,col) in computer_shots:
            return True
        else:
            computer_shots.add((row,col))

            if player_board[row][col] == variables.WATER:
                print(list(variables.row_column_names.keys())[(list(variables.row_column_names.values()).index(col+1))], row+1, end =' -> ')
                print("La máquina ha fallado, es tu turno!")
                return False
            else:
                print(list(variables.row_column_names.keys())[(list(variables.row_column_names.values()).index(col+1))], row+1, end =' -> ')
                print("La máquina ha tocado uno de tus barcos. Le vuelve a tocar")
                player_board[row][col] = variables.BOAT_DAMAGED
                return True

def end_game(board):
    '''
    Function that checks how many damaged ships there are in a board.
    If damaged boats are the same as the total, the game is over and someone wins
    Args: 
        board (Board Class Object) : The board where the damaged boats are counted

    Returns: False if game is over | True if it isn't over.
    '''
    cont = np.count_nonzero(board == variables.BOAT_DAMAGED)

    if cont == 20: # Each player has 20 lives (boat positions)
        return False
    else:
        return True
    
def bienvenida(player_id):
    print()
    print(f"¡Bienvenido/a {player_id} al juego de Hundir la Flota!")
    print("\nReglas del juego:")
    print("1. Eres tú contra la máquina.")
    print("2. Cada uno, tiene un tablero de 10x10, que solo puede ver el.")
    print("3. Tienes 10 barcos de diferentes dimensiones colocados aleatoriamente en tu tablero.")
    print("4. El objetivo es hundir todos los barcos de tu oponente antes de que él hunda los tuyos.")
    print("5. Elige las coordenadas para atacar en el tablero de tu oponente y trata de adivinar la ubicación de sus barcos. Si aciertas, tienes otro turno.")
    print("6. Gana el jugador que hunda todos los barcos del oponente primero.")

    print("\nSímbolos en el tablero:")
    print("  💧: Agua")
    print("  💀: Barco tocado")
    print("  💥: Disparo fallido")

    print("\n¡Buena suerte, capitán!")

