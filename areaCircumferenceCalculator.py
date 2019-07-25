import math

print("This program will ask for the radius of a circle then calculate the area and circumference.")
print()
print()

# get radius - convert it from a string to a float
radius=float(input("please enter radius: "))

# do the math. Notice syntax for pi
area=math.pi*radius**2
circumference=math.pi*radius*2

# output results
print("Given a circle with radius =", radius)
print("The area =",area,"and the circumference =",circumference)
