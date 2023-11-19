# Punto de entrada de la aplicación para ejecutar el juego

from src.classes import *
from src.funciones import *
from src.variables import *

def main():
    player_id = input("Enter your name: ")

    if player_id == "demo":
        battleship_demo = Game()
        battleship_demo.play_demo(player_id)

    else:
        battleship_game = Game()
        battleship_game.play(player_id)
    

if __name__ == "__main__":
    main()


