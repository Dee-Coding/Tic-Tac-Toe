# Creating a 3x3 board
board = [["", "", ""], ["", "", ""], ["", "", ""]]

players = ["X", "O"]


def print_board(board):
    for i in range(3):
        for j in range(3):
            # Print numbered cells if empty, else print the symbol
            cell = board[i][j] if board[i][j] != "" else 3 * i + j + 1
            print(cell, end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-" * 9)


# Handling players moves and update the board
def player_move(board, player_symbol):
    print(f"Player {player_symbol}, it's your turn!")
    while True:
        try:
            cell_number = int(input("Enter cell number (1 to 9): "))
            if 1 <= cell_number <= 9:
                row = (cell_number - 1) // 3
                col = (cell_number - 1) % 3
                if board[row][col] == "":
                    board[row][col] = player_symbol
                    break
                else:
                    print("Cell is already taken. Try again.")
            else:
                print("Invalid cell number. Try again.")
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
    play_again = True

    while play_again:
        current_player = 0

        # Ask the user what symbol they want to play with
        while True:
            player_choice = input("Do you want to play with 'X' or 'O'? ").upper()
            if player_choice == "X":
                current_player = 0
                break
            elif player_choice == "O":
                current_player = 1
                break
            else:
                print("Invalid choice. Please enter 'X' or 'O'.")

            # reset board for a new game
            for i in range(3):
                for j in range(3):
                    board[i][j] = ""

        while True:
            print("Tic Tac Toe")
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
            current_player = (current_player + 1) % 2
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n) ").lower() == "y"


if __name__ == "__main__":
    main()
