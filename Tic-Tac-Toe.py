def print_board(board):
    # Print the current state of the game board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check if the specified player has won
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    # Check if the board is full (a tie)
    return all(cell != " " for row in board for cell in row)

def main():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        print(f"Player {current_player}, it's your turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            # Check for invalid moves
            print("Invalid move. Try again.")
            continue

        # Update the game board with the player's move
        board[row][col] = current_player

        if check_win(board, current_player):
            # Check if the current player has won
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        elif is_board_full(board):
            # Check for a tie
            print_board(board)
            print("It's a tie! The game is over.")
            break

        # Switch to the other player's turn
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
