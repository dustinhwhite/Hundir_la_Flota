# Punto de entrada de la aplicación para ejecutar el juego

from src.classes import *
from src.funciones import *
from src.variables import *

def main():

    player_id = input("Para comenzar, introduce tu nombre: ")
    bienvenida(player_id)

    if player_id == "demo":
        time.sleep(5)
        battleship_demo = Game()
        battleship_demo.play_demo(player_id)

    else:
        time.sleep(5)
        battleship_game = Game()
        battleship_game.play(player_id)
    

if __name__ == "__main__":
    main()


