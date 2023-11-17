# Punto de entrada de la aplicación para ejecutar el juego

from src.classes import *
from src.funciones import *
from src.variables import *

def main():
    # Create a new game instance
    battleship_game = Game()
    
    # Start the game
    battleship_game.play()

# This conditional checks if your script is being run directly (as opposed to being imported)
if __name__ == "__main__":
    main()