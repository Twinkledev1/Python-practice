
import random

def set_difficulty_level():
    

    while True: 
       difficulty = input("choose difficulty (easy, medium , hard):   ").lower()

       if difficulty == "easy":
           number_1 = random.randint(1,50)
           print("you enter this number", number_1)
           break

       elif difficulty == "medium":
           number_2 = random.randint(1,100)
           print("you enter this number", number_2)
           break
       
       elif difficulty == "hard":
            number_3 = random.randint(1,200)
            print("you enter hard, i am choosing number from 1 to 200 ")
            break

    else:
      number_3= random.randint(1,200)
      print("you enter this number", number_3)


set_difficulty_level()