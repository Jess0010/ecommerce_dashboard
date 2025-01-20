"""Modified from https://www.geeksforgeeks.org/python-program-implement-rock-paper-scissor-game/


Modifications since rps_v1.1 include:

- The question asking for a valid choice will break if the input is not an integer. This can be resolved either by:
    - Checking if the input is one of the valid strings: while choice not in ['1', '2', '3']
    - Using a try except loop nested in a recursive function. This is preferred as it will generalise. 
- There can never be a draw, as the code in the loop "while comp_choice == choice" asks the computer to redraw until 
    there is not a draw. I have chosen to allow draws, but alternatively the player could be told there is a draw and 
    that the computer is redrawing.
- The if statements check more things than are necessary. E.g. if there is a draw, there is no need to check if choice == 1. 
    Turning the whole set into one nested if statement clarifies what is going on and what the outcomes could be.
- The while loop is always set to True, so it relies on a break to exit. This is not recommended, so we can create an 
    extra parameter, playing, that we set to False when the player wants to end.
- Started to move the code into functions. 
- Started to remove hardcoding of Rock, Paper and Scissors and standardising the capitalisation by having a choice_options variable
    and using the order of the list to determine the choice number.
"""

# import random module
import random

choice_options = ["Rock", "Paper", "Scissors"]

num_choices = len(choice_options)

# print multiline instruction
# perform string concatenation of string
print(
    "Winning rules of the game ROCK PAPER SCISSORS are :\n"
    + "Rock vs Paper -> Paper wins \n"
    + "Rock vs Scissors -> Rock wins \n"
    + "Paper vs Scissors -> Scissors wins \n"
)

def get_user_choice():
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

playing = True
while playing:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the input from user

    choice = get_user_choice()

    # initialize value of choice_name variable
    # corresponding to the choice value
    choice_name = choice_options[choice - 1]

    # print user choice
    print("User choice is \n", choice_name)
    print("Now its Computers Turn....")

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, num_choices)

    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    comp_choice_name = choice_options[comp_choice - 1]

    print("Computer choice is \n", comp_choice_name)
    print(choice_name, "Vs", comp_choice_name)

    # we need to check of a draw
    if choice == comp_choice:
        print("Its a Draw =>\n", end="")
        result = "DRAW"
    elif choice == 1:
        if comp_choice == 2:
            print("paper wins =>\n", end="")
            result = "Paper"
        elif comp_choice == 3:
            print("Rock wins =>\n", end="")
            result = "Rock"
        else:
            raise ValueError("Invalid choice")
    elif choice == 2: 
        if comp_choice == 1:
            print("paper wins =>\n", end="")
            result = "Paper"
        elif comp_choice == 3:
            print("Scissors wins =>\n", end="")
            result = "Scissors"
        else:
            raise ValueError("Invalid choice")
    elif choice == 3:
        if comp_choice == 1:
            print("Rock wins =>\n", end="")
            result = "Rock"
        elif comp_choice == 2:
            print("Scissors wins =>\n", end="")
            result = "Scissors"
        else:
            raise ValueError("Invalid choice")
    else:    
        raise ValueError("Invalid choice")
    
    print("Do you want to play again? (Y/N)")
    # if user input n or N then condition is True
    ans = input().lower()
    if ans == "n":
        playing = False

# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")
