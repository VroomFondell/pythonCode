# Derek Sleeper, HW1, build sample one, 4/5/16
# This program will run the user through one MadLib
# style word game one time.

# The original story was this:
# The wombat crept through my living room.
# It stopped suddenly to listen.
# Just then, a beligierent Yokel came bursting onto the scene!
# "Where is my collection of Chuck Norris commemerstive plates?!"

# opening greetings
print('Welcome to the game.')
print('We will be playing russian roulette with your closeset family members')
print('I am kidding. Sort of.... ,meat bag.')

# input set
animal=input('What is te first animal that comes to mind?')
verb2=input('Now we need a verb ending in "ed".')
loc=input('What was the last place you took a nap?')
adj4=input('Now we need an adjective that ends in "ly".')
adj5=input('And now for any olde adjective.')
noun=input('Something a grandparent might have tucked away in a closet that they wish to keep secret.')

# output set
print('The',animal,verb2,'through',loc,'.')
print('It stopped',adj4,'to listen.')
print('Just then, a',adj5,'yokel came bursting onto the scene!')
print('"Where is my',noun,'?!"')

# I started this assignment with a set of index cards and a notion
# to confine the story to one side of one card.
# On another set of index cards, I wrote out the blocking for
# how I thought the program should look.
# After having the script and story blocked out, I wrote them into IDLE.
# My test phase could be summed up by the phrase "Ham Fisting"
# All in all, it worked about as well as expected. Though I quickly learned
# how easy it is to miss end quotes and closing parenthesis.
# Next time, I will write more detailed code before hand. Maybe alternate pen colors in said writing.
