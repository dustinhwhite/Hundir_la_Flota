import random 
import numpy as np
import tabulate
import src.variables as variables
import src.funciones as funciones


class Board:
    def __init__(self, player_id = "Computer", size=variables.SIZE, boat_symbol=variables.BOAT, boat_sizes=variables.BOAT_SIZES):
        self.player_id = player_id
        self.size = size
        self.boat_symbol = boat_symbol
        self.boat_sizes = boat_sizes
        self.board = funciones.initial_board()
        self.boats_placed = {key: 0 for key in boat_sizes} # Count boats in boat sizes, each value starts in 0 

        if self.player_id != "Computer":
            self.display_welcome_message()  

    def display_welcome_message(self):
        print (f"Welcome {self.player_id}! Let's play Battleship! May the odds be ever in your favour")

    def is_space_free (self, row, col, boat_size, orientation):
        if orientation == 'E':  # East
            if col + boat_size > self.size: # Check if end position of the boat is off the board
                return False
            return np.all(self.board[row, col: col + boat_size] == "~")
        elif orientation == 'W':  # West
            if col - boat_size < -1:    
                return False
            return np.all(self.board[row, col - boat_size + 1: col + 1] == "~")
        elif orientation == 'S':  # South
            if row + boat_size > self.size:
                return False
            return np.all(self.board[row: row + boat_size, col] == "~")
        else:  # North
            if row - boat_size < -1:
                return False
            return np.all(self.board[row - boat_size + 1: row + 1, col] == "~") # Check if the vertical space is free

    def place_boat(self, row, col, boat_size, orientation): 
        if orientation == 'E':  # East
            for i in range(boat_size):
                self.board[row, col + i] = self.boat_symbol
        elif orientation == 'W':  # West
            for i in range(boat_size):
                self.board[row, col - i] = self.boat_symbol
        elif orientation == 'S':  # South
            for i in range(boat_size):
                self.board[row + i, col] = self.boat_symbol
        else:  # North
            for i in range(boat_size):
                self.board[row - i, col] = self.boat_symbol

    def place_all_boats(self):
        for boat_size in self.boat_sizes:   # Go through each boat size defined in BOAT_SIZES
            required_boats_count = self.boat_sizes[boat_size]   # Get the number of boats of this size we need to place

            while self.boats_placed[boat_size] < required_boats_count:  # Keep placing boats until we have placed the required #
                orientation = random.choice(['N', 'S', 'E', 'W'])    # Generates orientation variable random choice
                row = np.random.randint(0, self.size)   # Generate a random starting position for the boat
                col = np.random.randint(0, self.size)

                if orientation:   
                    col = np.random.randint(0, self.size - boat_size + 1)
                else:
                    row = np.random.randint(0, self.size - boat_size + 1)
            
                if self.is_space_free (row, col, boat_size, orientation): # Check if the boat can be placed at the starting position
                    self.place_boat(row, col, boat_size, orientation) # If it can, place the boat on the board
                    self.boats_placed[boat_size] += 1   # Increase the count of boats placed for this size

    def display_board(self):
        '''
        Function that visually prints the player's ship board and their shooting board on the screen.

        Args: 
            self (Board Class Object) : The board to print in console

        Returns : None
        '''
        print(tabulate(self.board.tolist(),headers=variables.row_column_names.keys(), showindex=variables.row_column_names.keys(),tablefmt="rounded_grid",stralign='center'))


class Game:

    def __init__(self):
        pass


    def play(self):
        # Crear tableros para jugador:
        player_board = Board()
        player_tracking_board = funciones.initial_board()

        # Crear tablero para maquina:
        computer_board = Board()

        # Llenar tablero con barcos:
        player_board.place_all_boats()
        computer_board.place_all_boats()

        in_progress = True
        players_turn = True
        computer_shots = set()

        while in_progress:
                
            if players_turn:
                player_board.display_board()
                print(tabulate(player_tracking_board.tolist(),headers=variables.row_column_names.keys(), showindex=variables.row_column_names.values(),tablefmt="rounded_grid",stralign='center'))
                print("----- ES TU TURNO -----")
                coordinates = funciones.get_guess(player_tracking_board)
                acierto = funciones.player_shot(player_tracking_board, computer_board.board, coordinates)

                if acierto:
                    if not funciones.end_game(computer_board.board):
                        print("¡Enhorabuena, has ganado!")
                        break
                    print("Has acertado ! Tienes otro turno")
                    continue 
                else:
                    print("----- TURNO DE LA MÁQUINA -----")
                    players_turn = False

            else:
                acierto = funciones.computer_shot(player_board.board, computer_shots)
                if acierto:
                    if not funciones.end_game(player_board.board):
                        print("Ha ganado la máquina :( Hasta la próxima !")
                        break
                    continue
                else:
                    players_turn = True