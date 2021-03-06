# A program written by Derek Sleeper
# In which a game is played where three options are available
# The game goes something like; a>b,b>c,c>a


# import random number generator to be used for the computers input
import random


# the opening message to give the user an idea of what is going to happen within the program
# though does assume a certain amount of outside knowledge
# I feel rock, paper, scissors is common knowledge enough within our culture to
# not warrant to much explanation
def opening():
    print("Welcome to the game of rock paper scissors. If you win, you get to keep\n"
          "your access to the on board oxygen supply.\n"
          "If you lose, we won't get to play anymore....")


# this function prompts the user for an input to denote choice of game state related to them.
# the function then corrects for common inaccuracies and will re prompt user for information
# if the previous input fell outside the scope of what could be corrected for
def player_input():
    player = input("Enter your choice;\n"
                   "'r' for rock;\n"
                   "'p' for paper;\n"
                   "'s' for scissors;\n"
                   "Which will it be? ")
    player = player.lower()
    player = player.strip()

    if player != 'r' and player != 'p' and player != 's':
        print("I'm sorry, you seem to be having trouble. \n"
              "Please reenter a valid input option.")
        (player_input())
    if player == "r":
        player = "rock"
    elif player == "p":
        player = "paper"
    elif player == "s":
        player = "scissors"
    return player


# this function uses the module imported to create a random number and assign that number
# to a value that can be directly compared with the user input
def computer_input():
        computer = random.randint(0, 2)
        if computer == 0:
            computer = "rock"
        elif computer == 1:
            computer = "paper"
        elif computer == 2:
            computer = "scissors"
        return computer


# the game_main function determines the outcome of the game by comparing the user input
# to the computer input and makes a series of determination to come up with a winner
# if the game_main function determines there is no winner, it will re run the input
# functions and determination logic until a winner can be determined
def game_main(player, computer):
    if player == computer:
        print("Draw! We will play again.")
        main()
    elif player == "rock":
        if computer == "paper":
            print("I'm sorry, your access privileges have been terminated.")
        else:
            print("Hurray! You get to keep breathing.")
    elif player == "paper":
        if computer == "rock":
            print("My, you are a fortunate biological entity.")
        else:
            print("Well, good bye...")
    elif player == "scissors":
        if computer == "rock":
            print("For you, that is unfortunate.")
        else:
            print("You may continue exchanging gasses with your internal chest sacks.")


# this function is set to reassert what the user had chosen at the beginning of the game and reveal
# the chosen input of the program so they may feel they are actually playing a game and
# not having a arbitrary determination made
def game_end_display(player, computer):
    print("Your choice: " + player + "\nHal's choice: " + computer + "")


# the main function is this program performs a few separate functions.
# foremost, the main function orders the sequence in which the individual functions
# should be executed. additionally, the main function stores the player and computer variables
# to be passed to and from from the various functions as the program runs
def main():
    opening()
    player = player_input()
    computer = computer_input()
    game_main(player, computer)
    game_end_display(player, computer)


# the call to main to get the whole thing off and running
main()




# How did I start?
# I started by sketching out what the program should do. I then broke that sketch into pieces.
# These pieces turned into the main() function.


# Where did I get stuck?
# I had a bit of trouble with invalid inputs for the player_input() function. I ended up
# writing way more code than I needed and it still left some invalid input options open.
# The player_input function still has bugs. Specifically, the recall of player_input creates a second
# global for player_input and I'm not sure how to get around that. Returning the incorrect input passes
# all the way through the program. I am not sure how to stop it going back through more than one function.

# How did I un-stick?
# Still kind of stuck.


# How was testing done?
# I wrote the opening and closing first, as I figured they would be the easiest. And having the
# display function complete, I could use it to see what the program was outputting if there were no syntax
# errors. I wrote the main function next and simply defined player and computer.
# The next piece was computer_input. I replaced manually defining computer with the computer_input function
# to ensure the code was still working. Building off that was the player_input. The player_input function
# is very similar to the computer_input function, though includes the headache that is correcting for
# invalid input. So I was then able to test not only the two input functions, but the game function, and
# and the display function simultaneously. I like this as it allows me to see where the code is not
# properly passing information. Also, this allowed me to build and test the main() function as I went.
# I effectively built the main function one piece at a time while building the other functions.


# What did I learn?
# The smaller and more cohesive the original documentation list is, the easier it is to define
# functions and their parameters. Also, a lot of input issues can be solved by more clearly stating
# to the user what valid input looks like. Explaining why is also helpful.


# What would I do differently next time?
# I still think I could do better at physically mapping out how information need to be passed
# between functions before getting into writing the definitions of the functions. Also, if I were
# to do this again, I would like to add a "play again?" function to the end of the game. Something
# requiring input from the user to call main. Though having trouble with the correction of invalid inputs,
# I am not sure if that is the correct approach.
