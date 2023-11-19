### Bienvenidos a Battleship Game!!!, este juego es un proyecto grupal para The Bridge, Data Science bootcamp PT 2023.

![Barco](https://static.wikia.nocookie.net/listofdeaths/images/7/74/Battleship_poster.jpg/revision/latest?cb=20220318035016)

<br>


## Contenidos

   1. [ A - Cómo funciona el juego](#A)
   1. [B - Classes](#B) 
   1. [C - Functions](#C)
   1. [D - Main.py](#D)
   1. [F - Requirements](#F)
   1. [G - Collaborators and Tasks](#G)
    



<a name="A"></a>
#### A - ¿Cómo funciona el juego?
Este es un juego de dos jugadores: tú y la máquina. El juego se desarrolla en un tablero de 10 x 10 posiciones donde aleatoriamente se colocan los barcos.   

Se juega con:

* 4 barcos de 1 posición de eslora
* 3 barcos de 2 posiciones de eslora
* 2 barcos de 3 posiciones de eslora
* 1 barco de 4 posiciones de eslora

El Jugador y la máquina tienen un tablero con barcos, y se trata de ir “disparando” y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde. 
  
El juego funciona por turnos y empiezas tú. En cada turno, disparas a una coordenada del tablero adversario. Si aciertas, te vuelve a tocar. En caso contrario, le toca a la máquina. En los turnos de la máquina, si acierta también le vuelve a tocar. 



<a name="B"></a>
#### B - Classes

Class Board:

    class to represent the game board for the game 
    
    
def is_ space_ free (self, row, col, boat_size, is_ horizontal):

        Function to check horizontal or orientation
        
def place_boat(self, row, col, boat_size, is_horizontal): 

        Place the boats on the board


def display_board(self):

        Display board

<a name="C"></a>
#### C - Functions
def initial_board():
    
    
    Function that initializes a "water" board without boats.
  
    
def initial_board():

    
    create a two dimensional array
    
    
def display_boards(player_board, player_tracking_board):

    displays the two boards 

def get_guess(): 

    Prompts the user for a row and column to attack. The
    return value is a board position in (row, column) format.
    

def initial_board():
    
    
    Function that initializes a "water" board without boats.
    
   
def get_guess(): 

    Prompts the user for a row and column to attack. The
    return value is a board position in (row, column) format.
    
def computer_shot(player_board, computer_shots):

    
    Checks whether or not position is occupied by a ship in the player board. 
    A hit is registered when position occupied by a ship and position not hit previously. 
    A miss occurs otherwise.
        
 def end_game(board):
 
    
    Function that checks how many damaged ships there are in a board.
    If damaged boats are the same as the total, the game is over and someone wins
    
        
<a name="B"></a>
#### D - Main.py

From this file we can execute the game
<a name="E"></a>
#### E - Requirements
Python 3.11.   
Pandas 2.1.1.   
Numpy 1.26.   
<a name="G"></a>
#### G - Collaborators and Tasks
Beatriz García@ <beatriz.bgd@gmail.com>     

* Printear tableros jugador
* Obtener el tablero inicial (todo estado agua)
* Imprimir por pantalla tanto el tablero de barcos del jugador, como el tablero de sus disparos de una forma visual.
* Añadir a cada tablero un nombre identificativo.
* Función disparo máquina* Crear Clase Game
* READ.me

Dustin White @ <dustinwhite@gmail.com>. 

* Git: Crear el repositorio y la estructura del mismo.
* Variables.py: Establecer las constantes del juego
* Crear clase Board.
* Inicializar un tablero y colocar los barcos, tanto de forma horizontal, como de forma vertical, todo de forma aleatoria.
* Al colocar los barcos, se comprueba que no están superpuestos y que el barco se puede colocar sin salirse del tablero.
READ.me
  
Juan Miguel López Piñero @ <juanmiguelopezpinero@icloud.com>. 
     
* Función recibir coordenadas del jugador
* Función disparo jugador: Recibe el output con las coordenadas y comprueba en el tablero de barcos de la máquina el estado que hay (agua, barco). Por último, modifica el tablero de disparos del jugador. Mostrar una salida: agua, tocado o disparo ya efectuado.
* Actualizar el juego modificando el tablero con un símbolo de acierto o fallo 
* READ.me

