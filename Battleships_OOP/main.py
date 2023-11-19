# Punto de entrada de la aplicación para ejecutar el juego

from src.classes import *
from src.funciones import *
from src.variables import *

# def main():
#     player_id = input("Enter your name: ")

#     # Create a new game instance
#     battleship_game = Game()
    
#     # Start the game
#     battleship_game.play(player_id)

# # This conditional checks if your script is being run directly (as opposed to being imported)
# if __name__ == "__main__":
#     main()

def main():
    player_id = input("Enter your name: ")
    print(f"Player ID entered: {player_id}")  # Debugging statement

    battleship_game = Game()
    print("Game instance created")  # Debugging statement

    battleship_game.play(player_id)
    

if __name__ == "__main__":
    main()
