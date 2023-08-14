# Creating a 3x3 board
board = [["", "", ""], ["", "", ""], ["", "", ""]]

players = ["X", "O"]
# Display the board in terminal
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Handling players moves and update the board
def player_move(board, player_symbol):
    print(f"Player {player_symbol}, it's your turn!")
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "":
                board[row][col] = player_symbol
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")


# Check if a player wins
def check_win(board, player_symbol):
    for row in board:
        if all(square == player_symbol for square in row):
            return True

    for col in range(3):
        if all(board[row][col] == player_symbol for row in range(3)):
            return True

    if all(board[i][i] == player_symbol for i in range(3)) or all(
        board[i][2 - i] == player_symbol for i in range(3)
    ):
        return True

    return False


# check if it is a tie
def check_tie(board):
    for row in board:
        if "" in row:
            return False
    return True


# main loop
def main():
    
    current_player = 0
    while True:
        print_board(board)
        player_symbol = players[current_player]
        player_move(board, player_symbol)

        if check_win(board, player_symbol):
            print_board(board)
            print(f"Player {player_symbol} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        if current_player == 0:
            current_player = 1
        else:
            current_player = 0


if __name__ == "__main__":
    main()
