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


def Winner(board):
    global contMove
    if board[1] == "O" and board[2] == "O" and board[3] == "O":
        print("El ganador es el jugador")
        contMove = 9
    elif board[1] == "O" and board[5] == "O" and board[9] == "O":
        print("El ganador es el jugador")
        contMove = 9
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("El ganador es el jugador")
        contMove = 9
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("El ganador es el jugador")
        contMove = 9
    elif board[3] == "O" and board[6] == "O" and board[9] == "O":
        print("El ganador es el jugador")
        contMove = 9
    elif board[3] == "O" and board[5] == "O" and board[7] == "O":
        print("El ganador es el jugador")
        contMove = 9
    elif board[4] == "O" and board[5] == "O" and board[6] == "O":
        print("El ganador es el jugador")
        contMove = 9
    elif board[7] == "O" and board[8] == "O" and board[9] == "O":
        print("El ganador es el jugador")
        contMove = 9
    elif board[1] == "X" and board[2] == "X" and board[3] == "X":
        print("El ganador es la CPU")
        contMove = 9
    elif board[1] == "X" and board[5] == "X" and board[9] == "X":
        print("El ganador es la CPU")
        contMove = 9
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("El ganador es la CPU")
        contMove = 9
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("El ganador es la CPU")
        contMove = 9
    elif board[3] == "X" and board[6] == "X" and board[9] == "X":
        print("El ganador es la CPU")
        contMove = 9
    elif board[3] == "X" and board[5] == "X" and board[7] == "X":
        print("El ganador es la CPU")
        contMove = 9
    elif board[4] == "X" and board[5] == "X" and board[6] == "X":
        print("El ganador es la CPU")
        contMove = 9
    elif board[7] == "X" and board[8] == "X" and board[9] == "X":
        print("El ganador es la CPU")
        contMove = 9


def NextMove():
    global contMove
    while contMove <= 8:
        DrawMove(board)
        DisplayBoard(board)
        EnterMove(board)
        DisplayBoard(board)
        os.system('cls')
        Winner(board)
        NextMove()


DisplayBoard(board)
NextMove()
