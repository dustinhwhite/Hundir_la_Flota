
#  variables 
HIT_CHAR= "X"
MISS_CHAR= "O"
BLANK_CHAR= " "



def get_guess(self):
    """Prompts the user for a row and column to attack. The
    return value is a board position in (row, column) format.
    """
    row = input("Enter a row (A-J): ").upper()
    col = int(input("Enter a column (0-9): "))
    return (row, col)


def check_guess(self, position):
    """Checks whether or not position is occupied by a ship. A hit is
    registered when position occupied by a ship and position not hit
    previously. A miss occurs otherwise.
    param position: a (row,column) tuple guessed by user
    return: guess_status: True when guess results in hit, False when guess results 
    """
    row, col = position
    if self.board[row][col] == HIT_CHAR:
        print("Hit already, try again!")
        return False
    elif self.board[row][col] == BLANK_CHAR:
        print("Missed!")
        self.board[row][col] = MISS_CHAR
        return False
    else:
        print("Hit!")
        self.board[row][col] = HIT_CHAR
        return True



def update_game(self, guess_status, position):
    """Updates the game by modifying the board with a hit or miss
    symbol based on guess_status of position.
    param guess_status: True when position is a hit, False otherwise
    param position:  a (row,column) tuple guessed by user
    return: None
    """
    row, col = position
    if guess_status:
        self.board[row][col] = HIT_CHAR 
        print("Hit!")
    else:
        self.board[row][col] = MISS_CHAR
        print("Missed!")