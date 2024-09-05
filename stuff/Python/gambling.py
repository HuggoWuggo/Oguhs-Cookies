#i love men
from random import randint
import os
from time import sleep

print("Welcome to gamblingpy! Choose a number between 1 and 6, \nand if it matchs with the computers guess, you win!")
sleep(5)
while True:
    def get_amount():
        while True:
            amount = input("Enter amount: ")
            try:
                global val
                val = int(amount)
                if val >= 1 and val <= 7:
                    break
                elif val < 1:
                    print("Too low")
                elif val > 6:
                    print("Too high!")
            except ValueError:
                print("Amount must be a number, try again")
        return val

    get_amount()

    companswer = randint(1,6)

    print(companswer)

    if val == companswer:
        print("You won!")
        break

    else:
        print("incorrect try again")
        sleep(0.5)
