import random

print("="*20,"Welcome to Snake, Water, Gun Game!","="*20)

while True:
    computer = random.choice(['s', 'w', 'g'])
    user = input("Enter 's' for Snake, 'w' for Water, 'g' for Gun: ")

    print(f"\nComputer chose: {computer}")
    print(f"You chose: {user}\n")

    if user == computer:
        print("It's a tie!")
    else:
        if(user == 's' and computer == 'w') or (user == 'w' and computer == 'g') or (user == 'g' and computer == 's'):
            print("🎉🎉 You win! 🎉🎉\n")
        elif user not in ['s', 'w', 'g']:
            print("Invalid input! Please choose 's', 'w', or 'g'.\n")
        else:
            print("☺️ Computer wins! Better luck next time!\n")
            
    if(user not in ['s', 'w', 'g']): break