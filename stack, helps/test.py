import time
import threading
import os


timel = 5

def question():
    q = input("",)
    print(q)
    if q == "2":
        print("\nCorrect")
    else:
        exit("\nFalse, You lose!!")

def counter():
    timel = 5
    for i in range(0, timel):
        print("How much is 1+1?", timel)
        timel -= 1
        time.sleep(1)
        os.system("cls")


def timer(seconds):
    time.sleep(seconds)
    exit("\nTIMES UP, You lose!!")

def exit(msg):
    print(msg)
    os._exit(1)

def main():
    thread = threading.Thread(target=timer, args=(int("{}".format(timel)),))
    thread2 = threading.Thread(target=counter)
    thread.start()
    thread2.start()
    question()

if __name__ == "__main__":
    main()
