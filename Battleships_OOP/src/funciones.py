# Funciones no incluidas en las Clases

import numpy as np
import variables

def initial_board():
    '''
    Function that initializes a "water" board without boats.
    
    Returns: Numpy array 
    '''
    init_board = np.full((variables.SIZE,variables.SIZE), variables.WATER)
    return init_board