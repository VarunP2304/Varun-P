def print_board(board):
    # Print the current state of the board
    for row in board:
        print(" |  ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check if the current player has won the game
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Check if the board is completely filled
    return all(board[i][j] != "" for i in range(3) for j in range(3))

def tic_tac_toe():
    # Main function to run the Tic Tac Toe game
    board = [["" for _ in range(3)] for _ in range(3)]  # Initialize the empty board
    current_player = 'X'  # Start with player 'X'
    
    while True:
        print_board(board)  # Display the board
        
        # Get the current player's move
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        # Place the move on the board if the cell is empty
        if board[row][col] == "":
            board[row][col] = current_player
        else:
            print("Cell already occupied! Try again.")  # Prompt if cell is occupied
            continue

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")  # Announce the winner
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")  # Announce a tie
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()
