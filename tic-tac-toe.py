"""
Simple Tic Tac Toe game for 2 players
"""

# drawing the board
def printBoard(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# checking if we have a winner (rows / columns / diagonal)
def checkWinner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# main game function
def playGame():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    printBoard(board)

    # main loop
    while True:
        row = int(input("Enter the row (1-3): ")) -1
        col = int(input("Enter the column (1-3): ")) -1

        if row > 2 or row < 0 or col > 2 or col < 0:
            print("Sorry, please enter only 1-3")
            continue

        # ensure the input is valid
        if board[row][col] == " ":
            board[row][col] = current_player
            printBoard(board)

            if checkWinner(board, current_player):
                print(f"Player {current_player} wins!")
                break

            if all(all(cell != " " for cell in row) for row in board):
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

# starting here
if __name__ == "__main__":
    playGame()