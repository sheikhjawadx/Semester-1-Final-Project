import random

# Initialize global variables for scores and rounds
user_score = 0
comp_score = 0
current_round = 0
total_rounds = 3  # Number of rounds to play

# Game logic function
def logic(comp, user):
    if comp == user:
        return 0  # Draw
    elif (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0):
        return 1  # User wins
    else:
        return 2  # Computer wins

# Function to play a single round
def play_round():
    global user_score, comp_score, current_round

    # Choices mapped to names
    choices = ["Snake", "Water", "Gun"]

    # Get user's choice
    print("Choices: \n0 = Snake \n1 = Water \n2 = Gun")
    try:
        user_choice = int(input("Enter your choice (0/1/2): "))
        if user_choice not in [0, 1, 2]:
            print("Invalid choice! Please choose 0, 1, or 2.")
            return
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, or 2).")
        return

    # Computer's random choice
    comp_choice = random.randint(0, 2)

    # Determine the result
    result = logic(comp_choice, user_choice)

    # Prepare the result message
    user_text = choices[user_choice]
    comp_text = choices[comp_choice]
    print(f"\nRound {current_round + 1}:")
    print(f"You chose: {user_text}")
    print(f"Computer chose: {comp_text}")

    if result == 0:
        print("It's a Draw!")
    elif result == 1:
        print("You Won!")
        user_score += 1
    else:
        print("You Lost!")
        comp_score += 1

    # Increment the round counter
    current_round += 1

# Function to display the final result
def show_final_result():
    global user_score, comp_score

    # Determine the overall winner
    if user_score > comp_score:
        final_outcome = "Congratulations! You won the game!"
    elif user_score < comp_score:
        final_outcome = "Oops! The computer won the game!"
    else:
        final_outcome = "It's a Tie!"

    # Display the final scoreboard
    print("\nGame Over!")
    print(f"Final Scores:\nYou: {user_score}\nComputer: {comp_score}")
    print(final_outcome)

# Function to reset the game for a new session
def reset_game():
    global user_score, comp_score, current_round
    user_score = 0
    comp_score = 0
    current_round = 0

# Main function to run the game
def main():
    global current_round, total_rounds

    print("Welcome to the Snake-Water-Gun Game!")

    while True:
        # Play rounds until the total round limit is reached
        while current_round < total_rounds:
            play_round()

        # Show the final result
        show_final_result()

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            reset_game()
        else:
            print("Thanks for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    main()