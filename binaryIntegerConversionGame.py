# importing the needed module for random
import random


# win condition for the game
game_win = 8


# this text is displayed immediately upon running of the game
# it lays out the method and basic idea of the game to the user
def opening_display():
    print('Welcome to the game\n'
          'a number will be displayed\n'
          'and you will guess the binary equivalent.\n'
          'we play ten rounds,\n'
          'if you are correct', game_win, 'or more times,\n'
          'you have won the game')


# this function generates the random number to be guessed
# and displays the number to the user
def random_number(chosen_base):
#    target_number = random.randint(0, 100)
    target_number = 25
    binary = ""
    if chosen_base == 0:
        print('this is the number to guess: ', target_number, )
        return target_number

    else:
        while target_number > 0:
            binary = str(target_number % 2) + binary
            target_number //= 2
        print('this is the target number to guess: ', binary, )
        return binary


# this function captures the users guess to compared with the
# randomly generated number. This function captures as a string
# and verifies the inputted guess is indeed a binary number, re prompting
# the user for correct input if incorrect input is detected.
def player_guess(chosen_base):
    player_binary = ''
    if chosen_base == 0:
        verify_input = True
        while verify_input:
            binary = input('please enter you guess in binary form: ')
#            binary = '11001'
            for digit in binary:
                if digit not in ['0', '1']:
                    print('Entry error')
                    verify_input = True
                else:
                    verify_input = False
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        return decimal
    else:



#        player_number = 25
        player_number = int(input('please enter integer value'))
        while player_number > 0:
            player_binary = str(player_number % 2) + player_binary
            player_number //= 2
        return player_binary


# this function compares the randomly generated integer and the integer
# created from the conversion of the user string to evaluate
# if the user's guess is correct. This is where the point for a correct
# answer is awarded.
def compare(player_number, target_number, points):
    if player_number == target_number:
        print('Correct. You have earned a point.')
        points += 1
        return points
    else:
        print('No point earned.')
        points = points
        return points


# this is the control function for the number of iterations
# the game will run. It is also the storage node for number of
# rounds played and points awarded.
# As well, this function takes care of the information
# to be displayed at the beginning of each round by making use of
# data stored at this level.
def recursion():
    points = 0

    for iteration in range(1, 11):
        print('this is round', iteration)
        print('You have won', points, 'rounds so far')
        print('having lost', iteration - 1 - points)
        points = game(points)
    if points >= game_win:
        print('your score of', points, 'is enough to win')
    else:
        print('your score of', points, 'is not enough to win')


# this function controls the three primary functions of the game
# mechanics.
def game(points):
#    chosen_base = 0
#    chosen_base = 1
    chosen_base = random.randint(0, 1)
    target_number = random_number(chosen_base)
    player_number = player_guess(chosen_base)
    points = compare(target_number, player_number, points)
    return points


# the main function, in this case, is just here to provide a place to
# split the opening sequence from the game sequence.
def main():
    opening_display()
    recursion()


# and the call to make get it off the ground
main()


# I began the process for this program by making a note list of functions needed.
# this list went through a couple revisions, breaking it into smaller and smaller
# pieces until I was happy with how much each function needed to accomplish
# I wrote pseudocode for each function in no particular order. I looked at my notes
# and wrote what came to mind first to block out the flow and logic, then filled
# in what was needed with more proper syntax.

# Having already planned out the logic flows helped the general development and
# writing of this program go pretty well. I ran into hiccups with what levels
# pieces of data were being stored at. It took a fare amount of jiggering
# to get the right data at the right nodes to be able to pass information
# from one function to another with minimal conversion. I worked around this
# by using lots of scratch paper.

# Converting verifying and converting the user input was easily the most difficult
# piece for me. I originally had two function, one to capture data and one to
# convert data. I felt that was proving too cumbersome, and difficult, so I
# combined them to not have to cope with another level of data transfer.

# Testing was again pretty constant throughout the development of the program.
# anything that returns information, I asked to print so I could see what was
# being passed back up the tree. Also, for the generated and inputted values,
# i substituted a given quantity to shorten amount of time needed to test parts
# of the program other than the number generation code, and the user input
# capture code.

# Currently, the program falls short in verifying integer inputs
# from the user. As in crashes when a non integer is given.

# Next time, I will create a hard copy of program requirements to attach to
# my notes on program creation to ensure I do not lose track of requirements.
# Moving forward I will also make use of a new way to visualize logic nodes
# in my notations. It is much clearer and easier to follow than what I have been
# doing previously. There was an over sight
# and a functionality was lost in my note translations early on. It wasn't
# the final stages  did i notice that I had missed the function to alternate
# between game modes.
