import os
import msvcrt
import time

board = "\t[ ] [ ] [ ]\n" \
        "\t[ ] [ ] [ ]\n" \
        "\t[ ] [ ] [ ]\n"

allowed_keys = [55, 56, 57, 52, 53, 54, 49, 50, 51]

lastturn = "oturn"
iswon = 0
turncount = 0


# Controls the displayed keyboard and turns
def gameboard(board):
        print("\n")
        is_won(board)
        print(board)
        if lastturn == "oturn":
            # If game is won, Don't allow moves
            if turncount >= 8:
                print("DRAW, GOOD GAME!!")
                time.sleep(3)
            elif iswon == 1:
                is_won(board)
            elif iswon == 0:
                print("\t X's turn!")
                xturn(mygetch())
        else:
            if iswon == 1:
                is_won(board)
            elif iswon == 0:
                print("\t O's turn!")
                oturn(mygetch())


# Captures keypresses for x and oturn
def mygetch():
    playerchoice = ord(msvcrt.getch())
    return playerchoice


# Checks if one of the players has won the game
def is_won(board):
    global iswon
    if (board[2] == "X" and board[6] == "X" and board[10] == "X" or
            board[2] == "O" and board[6] == "O" and board[10] == "O"):  # top horizontal
        print("CONGRATULATIONS!!\n")
        iswon += 1
    elif (board[15] == "X" and board[19] == "X" and board[23] == "X" or
            board[15] == "O" and board[19] == "O" and board[23] == "O"):  # middle horizontal
        print("CONGRATULATIONS!!\n")
        iswon += 1
    elif (board[28] == "X" and board[32] == "X" and board[36] == "X" or
            board[28] == "O" and board[32] == "O" and board[36] == "O"):  # bottom horizontal
        print("CONGRATULATIONS!!\n")
        iswon += 1
    elif (board[2] == "X" and board[15] == "X" and board[28] == "X" or
            board[2] == "O" and board[15] == "O" and board[28] == "O"):  # left vertical
        print("CONGRATULATIONS!!\n")
        iswon += 1
    elif (board[6] == "X" and board[19] == "X" and board[32] == "X" or
            board[6] == "O" and board[19] == "O" and board[32] == "O"):  # middle vertical
        print("CONGRATULATIONS!!\n")
        iswon += 1
    elif (board[10] == "X" and board[23] == "X" and board[36] == "X" or
            board[10] == "O" and board[23] == "O" and board[36] == "O"):  # right vertical
        print("CONGRATULATIONS!!\n")
        iswon += 1
    elif (board[2] == "X" and board[19] == "X" and board[36] == "X" or
            board[2] == "O" and board[19] == "O" and board[36] == "O"):  # left top - right bottom
        print("CONGRATULATIONS!!\n")
        iswon += 1
    elif (board[10] == "X" and board[19] == "X" and board[28] == "X" or
            board[10] == "O" and board[19] == "O" and board[28] == "O"):  # right top - left bottom
        print("CONGRATULATIONS!!\n")
        iswon += 1


# Place X on player chosen position
def xturn(playerchoice):  # box move for slices is +4 row change is +1
    global board
    global lastturn
    global turncount
    if playerchoice == 55:  # num7
        if board[2] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:2] + "X" + board[3:]
            os.system("cls")
            lastturn = "xturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 56:  # num8
        if board[6] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:6] + "X" + board[7:]
            os.system("cls")
            lastturn = "xturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 57:  # num9
        if board[10] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:10] + "X" + board[11:]
            os.system("cls")
            lastturn = "xturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 52:  # num4
        if board[15] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:15] + "X" + board[16:]
            os.system("cls")
            lastturn = "xturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 53:  # num5
        if board[19] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:19] + "X" + board[20:]
            os.system("cls")
            lastturn = "xturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 54:  # num6
        if board[23] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:23] + "X" + board[24:]
            os.system("cls")
            lastturn = "xturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 49:  # num1
        if board[28] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:28] + "X" + board[29:]
            os.system("cls")
            lastturn = "xturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 50:  # num2
        if board[32] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:32] + "X" + board[33:]
            os.system("cls")
            lastturn = "xturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 51:  # num3
        if board[36] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:36] + "X" + board[37:]
            os.system("cls")
            lastturn = "xturn"
            turncount += 1
            gameboard(board)
    elif playerchoice not in allowed_keys:
        print("INCORRECT INPUT PLEASE TRY AGAIN!!!")
        time.sleep(1)
        os.system("cls")
        xturn(mygetch())


# Places O on player chosen location
def oturn(playerchoice):
    global board
    global lastturn
    global turncount
    if playerchoice == 55:  # Q
        if board[2] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:2] + "O" + board[3:]
            os.system("cls")
            lastturn = "oturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 56:  # W
        if board[6] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:6] + "O" + board[7:]
            os.system("cls")
            lastturn = "oturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 57:  # E
        if board[10] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:10] + "O" + board[11:]
            os.system("cls")
            lastturn = "oturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 52:  # A
        if board[15] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:15] + "O" + board[16:]
            os.system("cls")
            lastturn = "oturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 53:  # S
        if board[19] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:19] + "O" + board[20:]
            os.system("cls")
            lastturn = "oturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 54:  # D
        if board[23] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:23] + "O" + board[24:]
            os.system("cls")
            lastturn = "oturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 49:  # Z
        if board[28] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:28] + "O" + board[29:]
            os.system("cls")
            lastturn = "oturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 50:  # X
        if board[32] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:32] + "O" + board[33:]
            os.system("cls")
            lastturn = "oturn"
            turncount += 1
            gameboard(board)
    elif playerchoice == 51:  # C
        if board[36] != " ":
            print("Place occupied, please try again!")
            time.sleep(2)
            os.system("cls")
            gameboard(board)
        else:
            board = board[:36] + "O" + board[37:]
            os.system("cls")
            lastturn = "oturn"
            turncount += 1
            gameboard(board)
    elif playerchoice not in allowed_keys:
        print("INCORRECT INPUT PLEASE TRY AGAIN!!!")
        time.sleep(1)
        os.system("cls")
        gameboard(board)


if __name__ == "__main__":
    print("This is a game of TIC-TAC-TOE!!\n"
          "GAME BOARD is represented by this shape\n", board)
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
