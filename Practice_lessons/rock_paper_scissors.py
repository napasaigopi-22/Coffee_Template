import random

options = ['r','p','s']

def user_choice():
    while True:
        input_1 = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
        if input_1 not in options:
            print("You entered an invalid input.")
            continue
        else:
            return input_1
            
def get_computer_choice():
    computer_input = random.choice(options)
    print(f'computer_input: {computer_input}')
    return computer_input
    
def determine_winner(input_1, computer_input):
    if(input_1 == computer_input):
        print("Draw!")
    elif \
        (input_1 == 'r' and computer_input == 's') or \
        (input_1 == 'p' and computer_input == 'r') or \
        (input_1 == 's' and computer_input == 'p'):
        print("you win!")
    else:
        print("you lose!")
while True:
    
    player_pick = user_choice()
    
    computer_pick = get_computer_choice()
    
    determine_winner(player_pick, computer_pick)
    
    continue_to_play = input('continue (y/n):').lower()
    if(continue_to_play == 'n'):
        print("Thank you for playing! Come Again")
        break