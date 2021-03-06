# This program will take user inputs for the dimensions of a room, as well as
# the cost of some materials, and perform the required to calculations for
# amount, and cost, of materials required to complete the tasks required.
# These tasks will include; painting, trimming, lighting, ventilating, and flooring.

# user inputs for room calculations
print('\nThis program requires your input in regard to the dimensions of the room and cost of materials to be used.')
print('It will then calculate and return complex dimensions, amount of material required, and material costs.\n')
length = float(input('What is the length of the room, in feet? '))
height = float(input('What is the height of the room, in feet? '))
width = float(input('What is the width of the room, in feet? '))
paintCost = float(input('What is the cost, per gallon, of the paint to be used, in dollars? '))
floorCost = float(input('What is the cost, per square foot, of the flooring to be used? '))
print()

# calculations
import math

# regarding paint
areaWall = (length * height) * (.9)
areaCeil = length * width
areaPaint = areaWall + areaCeil
paintReq = math.ceil(areaPaint / 350)
paintCostTotal = paintReq * paintCost

# regarding light and air
roomVolume = length * width * height

# regarding trim length
roomTrim = (length * 2) + (width * 2)

# regarding flooring
roomFloor = math.ceil(length * width)
floorCostTotal = roomFloor * floorCost

# output
print('Please verify the information you have given.\n')

# verify inputs
print('The dimensions you gave were:\nLength:', length, '\nHeight:', height, '\nWidth:', width, '\n')
print('The costs you gave were:\nCost of paint:', paintCost, '\nCost of flooring:', floorCost, '\n')

# output for paint
print('The total area to be painted is:', areaPaint, 'sq.ft')
print('This will require', paintReq, 'gal. of paint.')
print('The total cost of the paint required is:$', paintCostTotal, '\n')

# output for flooring
print('The amount of flooring required will be: ', roomFloor, 'sq.ft')
print('The total cost of flooring will be:$', floorCostTotal, '\n')

# output for air and light
print('The volume of the room is:', roomVolume, 'cu.ft\n')

# output for trim
print('The required amount of trim will be:', roomTrim, 'lin.ft\n')


# I began this assignment by defining the variables that were going to be used.
# After I had defined the variables, I defined the required outputs.
# I then broke the program into sections defined by the input/output relations.

# During the process of figuring how the conversions were going to need to be done
# I most often ran into errors regarding mis-keyed variables. One piece I could not sort out
# is how to create a new line using the \n function in the same command line as a input
# function without moving the users' input insertion point to the next line.

# I tested my program in pieces as I assembled it. After having written the outline
# by hand, I created the input and output sections. I then built each block of conversions
# under the "regarding" headings and tested them as they were being completed to ensure
# each function was working correctly before moving to the next.

# The most prominent thing I am taking away from this assignment is the manner
# in which variables are named. I found I had to rename them a few times
# so that they made sense when reading the code to follow how the numbers
# they represented moved through the program. Next time I think I should spend more
# time working out variable names before begining the coding.
