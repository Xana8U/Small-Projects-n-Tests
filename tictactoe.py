import os
import msvcrt
import time
import sys

board = "\t[ ] [ ] [ ]\n" \
        "\t[ ] [ ] [ ]\n" \
        "\t[ ] [ ] [ ]\n"

allowed_keys = [113, 119, 101, 97, 115, 100, 122, 120, 99]

lastturn = "oturn"


# Controls the displayed keyboard and turns
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


# Captures keypresses for x and oturn
def mygetch():
    playerchoice = ord(msvcrt.getch())
    return playerchoice


# Checks if one of the players has won the game
def is_won(board):
    if board[2] == "X" and board[6] == "X" and board[10] == "X" or board[2] == "O" and board[6] == "O" and board[10] == "O":  # top horizontal
        print("CONGRATULATIONS!!")
    elif board[15] == "X" and board[19] == "X" and board[23] == "X" or board[15] == "O" and board[19] == "O" and board[23] == "O":  # middle horizontal
        print("CONGRATULATIONS!!")
    elif board[28] == "X" and board[32] == "X" and board[36] == "X" or board[28] == "O" and board[32] == "O" and board[36] == "O":  # bottom horizontal
        print("CONGRATULATIONS!!")
    elif board[2] == "X" and board[15] == "X" and board[28] == "X" or board[2] == "O" and board[15] == "O" and board[28] == "O":  # left vertical
        print("CONGRATULATIONS!!")
    elif board[6] == "X" and board[19] == "X" and board[32] == "X" or board[6] == "O" and board[19] == "O" and board[32] == "O":  # middle vertical
        print("CONGRATULATIONS!!")
    elif board[10] == "X" and board[23] == "X" and board[36] == "X" or board[10] == "O" and board[23] == "O" and board[36] == "O":  # right vertical
        print("CONGRATULATIONS!!")
    elif board[2] == "X" and board[19] == "X" and board[36] == "X" or board[2] == "O" and board[19] == "O" and board[36] == "O":  # left top - right bottom
        print("CONGRATULATIONS!!")
    elif board[10] == "X" and board[19] == "X" and board[28] == "X" or board[10] == "O" and board[19] == "O" and board[28] == "O":  # right top - left bottom
        print("CONGRATULATIONS!!")
    else:
        return


def is_occupied():


# Place X on player chosen position
def xturn(playerchoice): # box move for slices is +4 row change is +1
    global board
    global lastturn
    if playerchoice == 113:  # Q
        board = board[:2] + "X" + board[3:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    elif playerchoice == 119:  # W
        board = board[:6] + "X" + board[7:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    elif playerchoice == 101:  # E
        board = board[:10] + "X" + board[11:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    elif playerchoice == 97:  # A
        board = board[:15] + "X" + board[16:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    elif playerchoice == 115:  # S
        board = board[:19] + "X" + board[20:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    elif playerchoice == 100:  # D
        board = board[:23] + "X" + board[24:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    elif playerchoice == 122:  # Z
        board = board[:28] + "X" + board[29:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    elif playerchoice == 120:  # X
        board = board[:32] + "X" + board[33:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    elif playerchoice == 99:  # C
        board = board[:36] + "X" + board[37:]
        os.system("cls")
        lastturn = "xturn"
        gameboard(board)
    elif playerchoice not in allowed_keys:
        sys.stderr("INCORRECT INPUT PLEASE TRY AGAIN!!!")
        time.sleep(1)
        os.system("cls")
        xturn(mygetch())


# Places O on player chosen location
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
