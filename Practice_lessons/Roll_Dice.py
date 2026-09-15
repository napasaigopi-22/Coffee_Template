import random

while True:
    input_1 = input("Roll the dice? (y/n): ").lower()
    if(input_1 == "y"):
        player_1 = (random.randint(1,6))
        player_2 = (random.randint(1,6))
        print((player_1,player_2))
    elif(input_1 == "n"):
        print("Thanks for Playing!")
        break
    else:
        print("Invalid Input. Try Again!")

    