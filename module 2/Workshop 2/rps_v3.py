"""Modified from https://www.geeksforgeeks.org/python-program-implement-rock-paper-scissor-game/

Modifications since rps_v2 include:

- To remove the hard coding of the choices, we used a dict as the official source of truth on what options 
    there are and what beats what. This is done with the winners dict. The advantage is that the main 
    if-else stops being nested and is much shorter. Equally, there is no chance that a non-valid option is 
    chosen, so we can remove the raising or errors.
- This has also allowed the instructions to be generated based on the dict.
- It has also allowed the if statements to be simplified, as we can now use the dict to find out who won.
"""

# Import random module. We will use this to choose the computer's choice
import random

# Define the winning conditions for each choice
winners = {"Rock": "Scissors",
           "Paper": "Rock",
           "Scissors": "Paper"}

choice_options = list(winners.keys())

num_choices = len(choice_options)

# Set the game name to be the list of choices
game_name = ", ".join(choice_options)

# Start the multiline game instructions
print(f"Winning rules of the game {game_name} are :")

# Generate the winning conditions string
winner_description  = "\n".join([f"{choice} vs {winners[choice]} -> {choice} wins" for choice in choice_options])

print(winner_description)

def get_user_choice():
    """Get the user's choice and validate it. 
    If it is invalid, it will be asked again
    
    Returns: int
    """
    try:
        choice = int(input("Enter your choice :"))
        if choice > num_choices or choice < 1:
            print("Please enter a valid choice")
            return get_user_choice()
        else:
            return choice
    except ValueError:
        print("Please enter a valid choice")
        return get_user_choice()

# Create the playing options string
playing_options = "\n".join([f"{i} - {choice}" for i, choice in enumerate(choice_options, 1)])
playing_instruction = f"Enter your choice \n{playing_options} \n"

# Now start the main play loop
playing = True
while playing:
    print(playing_instruction)

    # Get the choice from user
    choice = get_user_choice()

    # Find the choice name from the list of choices
    choice_name = choice_options[choice - 1]

    # Provide player context
    print("User choice is \n", choice_name)
    print("Now its Computers Turn....")

    # Computer chooses randomly any number among the possible choices
    comp_choice = random.randint(1, num_choices)

    # Find the computer choice name from the list of choices
    comp_choice_name = choice_options[comp_choice - 1]

    # Provide player context
    print("Computer choice is \n", comp_choice_name)
    print(choice_name, "Vs", comp_choice_name)

    # Check who won
    if choice == comp_choice:
        print("Its a Draw =>\n", end="")
        result = "DRAW"
    elif comp_choice_name == winners[choice_name]:
        print(f"{choice_name} wins =>\n", end="")
        result = choice_name
    else:
        print(f"{comp_choice_name} wins =>\n", end="")
        result = comp_choice_name
    
    # Find out if the player wants to play again
    print("Do you want to play again? (Y/N)")
    # if user input n or N then condition is True
    ans = input().lower()
    if ans == "n":
        playing = False

# Finish the game with thanks
print("thanks for playing")
