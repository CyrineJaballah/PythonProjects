import random

# Initialize the game board
board = [[0] * 4 for _ in range(4)]

# Function to print the game board
def print_board():
    for row in board:
        print(' '.join(str(num) for num in row))
    print()

# Function to add a new tile (2 or 4) randomly to the board
def add_tile():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = random.choice([2, 4])

# Function to perform left swipe
def swipe_left():
    for row in board:
        # Merge tiles
        for i in range(3):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0
        # Shift tiles to the left
        temp = [num for num in row if num != 0]
        row[:] = temp + [0] * (4 - len(temp))

# Function to check if the game is over
def is_game_over():
    # Check if any 2048 tile is present
    for row in board:
        if 2048 in row:
            return True
    # Check if there are any empty cells
    for row in board:
        if 0 in row:
            return False
    # Check if any adjacent tiles can be merged
    for i in range(3):
        for j in range(3):
            if board[i][j] == board[i][j+1] or board[j][i] == board[j+1][i]:
                return False
    return True

# Main game loop
while True:
    print_board()
    if is_game_over():
        print("Game Over!")
        break
    direction = input("Enter direction (left, right, up, down): ")
    if direction == "left":
        swipe_left()
    # Add other direction handling code (right, up, down) here
    add_tile()
