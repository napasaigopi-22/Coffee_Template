import random
guess_number = random.randint(1,100)
count = 0
while True:
    try:
        input_1 = int(input("Guess the number between 1 and 100: "))
        count += 1
        if(input_1 > guess_number):
            print("Too High!")
        elif(input_1 < guess_number):
            print("Too Low!")
        else:
            print("Congratulations! you guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number.")

print("Total attempts :", count)

