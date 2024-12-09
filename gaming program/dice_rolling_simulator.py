import random

def rolldice():
    while True:
       
       rand_num = random.randint(1,6)

       print("Rolling the dice")

       print(f"You rolled a {rand_num}")
    

       again = input("Rolled again? (yes/no): ").lower()


      
       if again != "yes":
          print ("Goodbye!")
          break

rolldice()
       





       




                  
