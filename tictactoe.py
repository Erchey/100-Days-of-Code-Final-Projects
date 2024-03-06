theBoard = {'1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6',
            '7': '7', '8': '8', '9': '9'}

def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

def checkWinner(board, player):
    # Check rows, columns, and diagonals for a win
    return ((board['1'] == board['2'] == board['3'] == player) or
            (board['4'] == board['5'] == board['6'] == player) or
            (board['7'] == board['8'] == board['9'] == player) or
            (board['1'] == board['4'] == board['7'] == player) or
            (board['2'] == board['5'] == board['8'] == player) or
            (board['3'] == board['6'] == board['9'] == player) or
            (board['1'] == board['5'] == board['9'] == player) or
            (board['3'] == board['5'] == board['7'] == player))

def isBoardFull(board):
    return all(value != str(key) for key, value in board.items())


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = str(input())

    if move not in theBoard or theBoard[move] != move:
        print('Invalid move. Try again.')
        continue

    theBoard[move] = turn

    if checkWinner(theBoard, 'X'):
        printBoard(theBoard)
        print('X wins!')
        break
    elif checkWinner(theBoard, 'O'):
        printBoard(theBoard)
        print('O wins!')
        break
    elif isBoardFull(theBoard):
        printBoard(theBoard)
        print('The game is a tie!')
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    