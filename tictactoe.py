import os
import msvcrt
import time
import sys

board = "\t[ ] [ ] [ ]\n" \
        "\t[ ] [ ] [ ]\n" \
        "\t[ ] [ ] [ ]\n"

allowed_keys = [113, 119, 101, 97, 115, 100, 122, 120, 99]

lastturn = "oturn"


def gameboard(board):
        print("\n")
        is_won(board)
        print(board)
        if lastturn == "oturn":
            print("\t X's turn!")
            xturn(mygetch())
        else:
            print("\t O's turn!")
            oturn(mygetch())


def mygetch():
    playerchoice = ord(msvcrt.getch())
    return playerchoice


def is_won(board):
    if board[3] and board[7] and board[11] is "X" or board[3] and board[7] and board[11] is "O":  # top horizontal
        print("CONGRATULATIONS!!")
    elif board[16] and board[20] and board[24] is "X" or board[16] and board[20] and board[24] is "O":  # middle horizontal
        print("CONGRATULATIONS!!")
    elif board[29] and board[33] and board[37] is "X" or board[29] and board[33] and board[37] is "O":  # bottom horizontal
        print("CONGRATULATIONS!!")
    elif board[3] and board[16] and board[29] is "X" or "O":  # left vertical
        print("CONGRATULATIONS!!")
    elif board[7] and board[20] and board[33] is "X" or "O":  # middle vertical
        print("CONGRATULATIONS!!")
    elif board[11] and board[24] and board[37] is "X" or "O":  # right vertical
        print("CONGRATULATIONS!!")
    elif board[3] and board[20] and board[37] is "X" or "O":  # left top - right bottom
        print("CONGRATULATIONS!!")
    elif board[11] and board[20] and board[29] is "X" or "O":  # right top - left bottom
        print("CONGRATULATIONS!!")
    else:
        return 0


def is_occupied():


def xturn(playerchoice): # box move for slices is +4 row change is +1
    global board
    global lastturn
    if playerchoice == 113:  # Q
        board = board[:2] + "X" + board[3:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    if playerchoice == 119:  # W
        board = board[:6] + "X" + board[7:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    if playerchoice == 101:  # E
        board = board[:10] + "X" + board[11:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    if playerchoice == 97:  # A
        board = board[:15] + "X" + board[16:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    if playerchoice == 115:  # S
        board = board[:19] + "X" + board[20:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    if playerchoice == 100:  # D
        board = board[:23] + "X" + board[24:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    if playerchoice == 122:  # Z
        board = board[:28] + "X" + board[29:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    if playerchoice == 120:  # X
        board = board[:32] + "X" + board[33:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    if playerchoice == 99:  # C
        board = board[:36] + "X" + board[37:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    if playerchoice not in allowed_keys:
        sys.stderr("INCORRECT INPUT PLEASE TRY AGAIN!!!")
        time.sleep(1)
        os.system("cls")
        xturn(mygetch())


def oturn(playerchoice):
    global board
    global lastturn
    if playerchoice == 113:  # Q
        board = board[:2] + "O" + board[3:]
        os.system("cls")
        lastturn = "oturn"
        gameboard(board)
    if playerchoice == 119:  # W
        board = board[:6] + "O" + board[7:]
        os.system("cls")
        lastturn = "oturn"
        gameboard(board)
    if playerchoice == 101:  # E
        board = board[:10] + "O" + board[11:]
        os.system("cls")
        lastturn = "oturn"
        gameboard(board)
    if playerchoice == 97:  # A
        board = board[:15] + "O" + board[16:]
        os.system("cls")
        lastturn = "oturn"
        gameboard(board)
    if playerchoice == 115:  # S
        board = board[:19] + "O" + board[20:]
        os.system("cls")
        lastturn = "oturn"
        gameboard(board)
    if playerchoice == 100:  # D
        board = board[:23] + "O" + board[24:]
        os.system("cls")
        lastturn = "oturn"
        gameboard(board)
    if playerchoice == 122:  # Z
        board = board[:28] + "O" + board[29:]
        os.system("cls")
        lastturn = "oturn"
        gameboard(board)
    if playerchoice == 120:  # X
        board = board[:32] + "O" + board[33:]
        os.system("cls")
        lastturn = "oturn"
        gameboard(board)
    if playerchoice == 99:  # C
        board = board[:36] + "O" + board[37:]
        os.system("cls")
        lastturn = "oturn"
        gameboard(board)
    if playerchoice not in allowed_keys:
        sys.stderr("INCORRECT INPUT PLEASE TRY AGAIN!!!")
        time.sleep(1)
        os.system("cls")
        oturn(mygetch())



if __name__ == "__main__":
    print("This is a game of TIC-TAC-TOE!!\n"
          "GAME BOARD is represented by this shape\n"
          , board)
    time.sleep(1)
    os.system("cls")
    print("To place X or O, press one of the keys presented here:\n"
          "\t\t\t[Q] [W] [E]\n"
          "\t\t\t[A] [S] [D]\n"
          "\t\t\t[Z] [X] [C]\n")
    time.sleep(1)
    input("Press Enter to start a game!!")
    os.system("cls")
    gameboard(board)
