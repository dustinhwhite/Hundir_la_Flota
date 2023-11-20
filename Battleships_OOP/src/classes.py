import random 
import numpy as np
import tabulate as tabulate 
import src.variables as variables
import src.funciones as funciones
from rich import print as rprint

class Board:
    def __init__(self, player_id = "Computer", size=variables.SIZE, boat_symbol=variables.BOAT, boat_sizes=variables.BOAT_SIZES,boats={4: "🚢", 3: "⛴️", 2: "🚤", 1: "⛵"}):
        self.player_id = player_id
        self.size = size
        self.boat_symbol = boat_symbol
        self.boats=boats
        self.boat_sizes = boat_sizes
        #self.boats = boats
        self.board = funciones.initial_board()
        self.boats_placed = {key: 0 for key in boat_sizes} # Count boats in boat sizes, each value starts in 0 

        if self.player_id != "Computer":
            self.display_welcome_message()  

    def display_welcome_message(self):
        print (f"Let's go {self.player_id}! Let's play Battleship! May the odds be ever in your favour")
        print()

    def is_space_free (self, row, col, boat_size, orientation):
        if orientation == 'E':  # East
            if col + boat_size > self.size: # Check if end position of the boat is off the board
                return False
            return np.all(self.board[row, col: col + boat_size] == variables.WATER)
        elif orientation == 'W':  # West
            if col - boat_size < -1:    
                return False
            return np.all(self.board[row, col - boat_size + 1: col + 1] == variables.WATER)
        elif orientation == 'S':  # South
            if row + boat_size > self.size:
                return False
            return np.all(self.board[row: row + boat_size, col] == variables.WATER)
        else:  # North
            if row - boat_size < -1:
                return False
            return np.all(self.board[row - boat_size + 1: row + 1, col] == variables.WATER) # Check if the vertical space is free

    def place_boat(self, row, col, boat_size, orientation): 
        if orientation == 'E':  # East
            for i in range(boat_size):
                self.board[row, col + i] = self.boats[boat_size]
        elif orientation == 'W':  # West
            for i in range(boat_size):
                self.board[row, col - i] = self.boats[boat_size]
        elif orientation == 'S':  # South
            for i in range(boat_size):
                self.board[row + i, col] = self.boats[boat_size]
        else:  # North
            for i in range(boat_size):
                self.board[row - i, col] = self.boats[boat_size]

    def place_all_boats(self):
        try:
            for boat_size in self.boat_sizes:   # Go through each boat size defined in BOAT_SIZES
                required_boats_count = self.boat_sizes[boat_size]   # Get the number of boats of this size we need to place

                while self.boats_placed[boat_size] < required_boats_count:  # Keep placing boats until we have placed the required #
                    orientation = random.choice(['N', 'S', 'E', 'W'])    # Generates orientation variable random choice

                    if orientation in ['E', 'W']:  # Horizontal
                        row = np.random.randint(0, self.size)
                        col = np.random.randint(0, self.size - boat_size + 1)
                    else:  # Vertical ('N', 'S')
                        row = np.random.randint(0, self.size - boat_size + 1)
                        col = np.random.randint(0, self.size)
            
                    if self.is_space_free (row, col, boat_size, orientation): # Check if the boat can be placed at the starting position
                        self.place_boat(row, col, boat_size, orientation) # If it can, place the boat on the board
                        self.boats_placed[boat_size] += 1   # Increase the count of boats placed for this size
                

        except Exception as e:
            print(f"An error occurred: {e}")  # Exception handling

    def display_board(self):
        '''
        Function that visually prints the player's ship board and their shooting board on the screen.

        Args: 
            self (Board Class Object) : The board to print in console

        Returns : None
        '''
        print(tabulate.tabulate(self.board,headers=variables.row_column_names.keys(), showindex=variables.row_column_names.values(),tablefmt="rounded_grid",stralign='center'))


class Game:

    def __init__(self):
        pass

    def play(self, player_id):
        # Crear tableros para jugador:
        player_board = Board(player_id)
        player_tracking_board = funciones.initial_board()

        # Crear tablero para maquina:
        computer_board = Board()

        # Llenar tablero con barcos:
        player_board.place_all_boats()
        computer_board.place_all_boats()

        # in_progress = True
        players_turn = True
        computer_shots = set()

        while True:
                
            if players_turn:
                print("------------------------ TUS BARCOS ------------------------")
                player_board.display_board()
                print("------------------------ TUS DISPAROS ------------------------")
                print(tabulate.tabulate(player_tracking_board,headers=variables.row_column_names.keys(), showindex=variables.row_column_names.values(),tablefmt="rounded_grid",stralign='center'))
                
                print("----- ES TU TURNO -----")
                coordinates = funciones.get_guess(player_tracking_board)
                if coordinates == (99,99):
                    print ("Has abandonado el juego, hasta pronto!\n")
                    break
                else:
                    acierto = funciones.player_shot(player_tracking_board, computer_board.board, coordinates)

                    if acierto:
                        if not funciones.end_game(player_tracking_board):
                            print("¡Enhorabuena, has ganado!")
                            break
                        print("Has acertado ! Tienes otro turno\n")
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

    def play_demo(self, player_id):
        
        # Tableros del jugador:
        demo_player_board = Board(player_id)
        demo_player_tracking_board = funciones.initial_board()

        # Tableros de la máquina
        demo_computer_board = Board()

        # Llenar tablero con barcos:
        demo_player_board.place_all_boats()
        demo_computer_board.place_all_boats()

        players_turn = True
        computers_turn = True
        computer_shots = set()
        print("------- TABLERO CON LOS BARCOS DEL JUGADOR -------")
        demo_player_board.display_board()
        print("------- TABLERO CON LOS DISPAROS DEL JUGADOR -------")
        print(tabulate.tabulate(demo_player_tracking_board,headers=variables.row_column_names.keys(), showindex=variables.row_column_names.values(),tablefmt="rounded_grid",stralign='center'))
        print("------- TABLERO CON LOS BARCOS DE LA MÁQUINA -------")
        demo_computer_board.display_board()
        
        while True:
            print()
            test = int(input("¿Qué quieres probar?\n1. Disparo jugador\n2. Disparo máquina\n3. Fin del juego - Victoria jugador\n4. Fin del juego - Victoria máquina\n Introduzca un número del 1-4 : "))
            if (type(test) != int) or (test>4) or (test<1):
                print("Comando inválido. Introduzca un número del 1-4")
                continue

            else:
                if test == 1: # PROBANDO DISPARO DEL JUGADOR
                    print()
                    players_turn = True
                    while players_turn:
                        print("------- TABLERO CON LOS DISPAROS DEL JUGADOR -------")
                        print(tabulate.tabulate(demo_player_tracking_board,headers=variables.row_column_names.keys(), showindex=variables.row_column_names.values(),tablefmt="rounded_grid",stralign='center'))
                        print("SIMULANDO DISPARO DEL JUGADOR")
                        coordinates = funciones.get_guess(demo_player_tracking_board)
                        if coordinates == (99,99):
                            print ("Has abandonado el juego, hasta pronto!")
                            break
                        else:
                            acierto = funciones.player_shot(demo_player_tracking_board, demo_computer_board.board, coordinates)

                            if acierto:
                                if not funciones.end_game(demo_player_tracking_board):
                                    print("¡Enhorabuena, has ganado!")
                                    break
                                print("Has acertado ! Tienes otro turno")
                                continue 
                            else:
                                rprint("------- TABLERO CON LOS DISPAROS DEL JUGADOR -------")
                                print(tabulate.tabulate(demo_player_tracking_board,headers=variables.row_column_names.keys(), showindex=variables.row_column_names.values(),tablefmt="rounded_grid",stralign='center'))
                                print("----- TURNO DE LA MÁQUINA -----")
                                players_turn = False
                
                elif test == 2: # PROBANDO DISPARO DE LA MÁQUINA
                    print("SIMULANDO DISPARO DE LA MÁQUINA")
                    computers_turn = True
                    while computers_turn:
                        acierto = funciones.computer_shot(demo_player_board.board, computer_shots)
                        if acierto:
                            if not funciones.end_game(demo_player_board.board):
                                print("Ha ganado la máquina :( Hasta la próxima !")
                                break
                            continue
                        else:
                            demo_player_board.display_board()
                            computers_turn = False

                elif test == 3: # VICTORIA FORZOSA DEL JUGADOR
                    print("SIMULANDO VICTORIA DEL JUGADOR")
                    players_turn = True
                    while players_turn:
                        print("----------- TABLERO CON LOS BARCOS DE LA MÁQUINA -----------")
                        demo_computer_board.display_board()
                        print()
                        print("Toca uno de sus barcos para ver qué pasaría al tocar su última vida")
                        coordinates = funciones.get_guess(demo_player_tracking_board)
                        if coordinates == (99,99):
                            print ("Has abandonado el juego, hasta pronto!")
                            break
                        else:
                            acierto = funciones.player_shot(demo_player_tracking_board, demo_computer_board.board, coordinates)

                            if acierto:
                                if funciones.end_game(demo_player_tracking_board):
                                    print("¡Enhorabuena, has ganado!")
                                    break
                                print("Has acertado ! Tienes otro turno")
                                continue 
                            else:
                                print("----- TURNO DE LA MÁQUINA -----")
                                players_turn = False
                else: # VICTORIA FORZOSA DE LA MÁQUINA
                    print("SIMULANDO DERROTA DEL JUGADOR")
                    computers_turn = True
                    while computers_turn:
                        acierto = funciones.computer_shot(demo_player_board.board, computer_shots)
                        if acierto:
                            if funciones.end_game(demo_player_board.board):
                                print("----------- TABLERO CON LOS BARCOS DEL JUGADOR -----------")
                                demo_player_board.display_board()
                                print("Ha ganado la máquina :( Hasta la próxima !")
                                break
                            continue
                        else:
                            continue


