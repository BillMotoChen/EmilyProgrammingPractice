# 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.

# But because you can't buy 0.6 of a can of paint, the result should be rounded up to an integer.

import math

# Define a function called paint_calc() so that the code below works.
def paint_calc(height, width, cover):
    num_of_can = math.ceil((height * width) / cover)
    print(f"You will need {num_of_can} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)