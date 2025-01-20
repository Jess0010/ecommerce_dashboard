"""Modified from https://www.geeksforgeeks.org/python-program-implement-rock-paper-scissor-game/

Modifications since rps_v3 include:

- Moving the code into functions. This allows the code to be reused. 

"""

# Import random module. We will use this to choose the computer's choice
import random

def setup_game(winners):
    """Setup the game by getting the possible choices and the winning conditions
    
    Returns: tuple
    """
    # Get the possible choices
    choice_options = list(winners.keys())

    # Get the number of choices
    num_choices = len(choice_options)

    # Set the game name to be the list of choices
    game_name = ", ".join(choice_options)

    # Generate the winning conditions string
    winner_description  = "\n".join([f"{choice} vs {winners[choice]} -> {choice} wins" for choice in choice_options])

    # Create the playing options string
    playing_options = "\n".join([f"{i} - {choice}" for i, choice in enumerate(choice_options, 1)])
    playing_instruction = f"Enter your choice \n{playing_options} \n"

    # Start the multiline game instructions
    print(f"Winning rules of the game {game_name} are :")
    print(winner_description)

    return (choice_options, num_choices, playing_instruction)


def get_user_choice(num_choices):
    """Get the user's choice and validate it. 
    If it is invalid, it will be asked again
    
    Returns: int
    """
    try:
        choice = int(input("Enter your choice :"))
        if choice > num_choices or choice < 1:
            print("Please enter a valid choice")
            return get_user_choice(num_choices)
        else:
            return choice
    except ValueError:
        print("Please enter a valid choice")
        return get_user_choice(num_choices)

def game_main(winners):
    """Run the game through many rounds until the player chooses to stop"""

    choice_options, num_choices, playing_instruction = setup_game(winners)

    # Now start the main play loop
    playing = True
    while playing:
        game_run(choice_options, num_choices, playing_instruction)

        # Find out if the player wants to play again
        print("Do you want to play again? (Y/N)")
        # if user input n or N then condition is True
        ans = input().lower()
        if ans == "n":
            playing = False

    # Finish the game with thanks
    print("thanks for playing")

def game_run(choice_options, num_choices, playing_instruction):
    """Run a single round of the game"""

    print(playing_instruction)

    # Get the choice from user
    choice = get_user_choice(num_choices)

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
    
    
if __name__ == "__main__":

    # Define the winning conditions for each choice
    winners = {"Rock": "Scissors",
               "Paper": "Rock",
               "Scissors": "Paper"}
    game_main(winners)