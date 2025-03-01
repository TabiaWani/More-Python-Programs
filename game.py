import random

def get_user_choice():
    print("Choose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("Enter your choice (1/2/3): "))
    while choice not in [1, 2, 3]:
        print("Invalid choice. Please choose 1, 2, or 3.")
        choice = int(input("Enter your choice (1/2/3): "))
    return choice

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        return "You win!"
    else:
        return "Computer wins!"

def choice_to_string(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {choice_to_string(user_choice)}")
    print(f"Computer chose: {choice_to_string(computer_choice)}")
    
    result = determine_winner(user_choice, computer_choice)
    print(f"\n{result}")

if __name__ == "__main__":
    main()
