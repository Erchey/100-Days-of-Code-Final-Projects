import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def find_best_move(board):
    best_score = -float("inf")
    best_move = None
    for row, col in get_empty_cells(board):
        board[row][col] = "O"
        score = minimax(board, 0, False)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):
        return 1
    elif check_win(board, "X"):
        return -1
    elif len(get_empty_cells(board)) == 0:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            score = minimax(board, depth+1, False)
            board[row][col] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            score = minimax(board, depth+1, True)
            board[row][col] = " "
            best_score = min(score, best_score)
        return best_score

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    difficulty = input("Choose difficulty (easy, medium, hard): ")

    while True:
        print_board(board)

        if player == "X":
            while True:
                try:
                    row = int(input("Enter row (0, 1, 2): "))
                    col = int(input("Enter column (0, 1, 2): "))
                    if board[row][col] != " ":
                        print("Cell already taken. Try again.")
                    else:
                        board[row][col] = "X"
                        break
                except (ValueError, IndexError):
                    print("Invalid input. Try again.")
        else:
            if difficulty == "easy":
                row, col = random.choice(get_empty_cells(board))
            elif difficulty == "medium":
                if random.random() < 0.5:
                    row, col = random.choice(get_empty_cells(board))
                else:
                    row, col = find_best_move(board)
            else:
                row, col = find_best_move(board)

            board[row][col] = "O"

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif len(get_empty_cells(board)) == 0:
            print_board(board)
            print("It's a tie!")
            break

        player = "X" if player == "O" else "O"

play_game()