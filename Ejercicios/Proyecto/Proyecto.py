from random import randrange
import os
contMove = 0
board = {1: "1", 2: "2", 3: "3", 4: "4",
         5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}


def DisplayBoard(board):
    print("* * * * * * * * * * * * * * * * * *\n")
    for i in range(len(board)):
        i += 1
        if(i == 3 or i == 6 or i == 9):
            print(board[i], "    |")
            print("\n* * * * * * * * * * * * * * * * * *\n")
        elif i == 1 or i == 4 or i == 7:
            print("|   ", board[i], end="     ")
        elif i == 2 or i == 5 or i == 8:
            print("|   ", board[i], end="     |     ")


def DrawMove(board):
    movCPU = randrange(1, 10)
    if board[movCPU] == "O":
        DrawMove(board)
    else:
        print("la computadora hizo su movimiento\n Es tu turno")
        board[movCPU] = "X"
        global contMove
        contMove += 1
    return board[movCPU]


def EnterMove(board):
    movPlayer = int(input("Introduce un numero"))
    if movPlayer <= 9 and movPlayer >= 1 and board[movPlayer] != "X":
        board[movPlayer] = "O"
        global contMove
        contMove += 1
        return board[movPlayer]
    else:
        EnterMove(board)


def nextMove(contMove):
    while contMove <= 8:
        DisplayBoard(board)
        DrawMove(board)
        DisplayBoard(board)
        EnterMove(board)
        DisplayBoard(board)
        os.system('cls')
        nextMove(contMove)


nextMove(contMove)
