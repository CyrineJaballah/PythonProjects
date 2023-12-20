board = [' ' for _ in range(9)]
player = 'X'

# Function to display the Tic Tac Toe board
def display_board():
    row1 = f' {board[0]} | {board[1]} | {board[2]} '
    row2 = f' {board[3]} | {board[4]} | {board[5]} '
    row3 = f' {board[6]} | {board[7]} | {board[8]} '
    separator = '-----------'
    print(f'{row1}\n{separator}\n{row2}\n{separator}\n{row3}')

# Function to handle a player's move
def make_move(position):
    global player
    if board[position] == ' ':
        board[position] = player
        display_board()
        if check_winner(player):
            print(f'Player {player} wins!')
            return True
        if ' ' not in board:
            print("It's a tie!")
            return True
        player = 'O' if player == 'X' else 'X'
    else:
        print('Invalid move. Please try again.')

# Function to check if a player has won
def check_winner(player):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for positions in winning_positions:
        if all(board[pos] == player for pos in positions):
            return True
    return False

# Main game loop
def play_game():
    display_board()
    while True:
        position = int(input("Enter a position (0-8): "))
        if make_move(position):
            break

# Start the game
play_game()

input("Press Enter to exit...")
