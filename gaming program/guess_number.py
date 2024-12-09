import random

def guess_the_number():
    random_num = random.randint(1,100)
    print = ("I have enter a number ! can you guess it?")

    while True:

         guess_num = int(input("Enter the guess number: "))

         if guess_num < random_num:
            print("Too low. Try again! ")

         elif guess_num > random_num:

            print ("Too high. Try again!")

         else :
            print("Congatulation! you are successful.")

guess_the_number()