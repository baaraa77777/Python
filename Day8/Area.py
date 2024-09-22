#If 5sq.m requires 1 can of paint. How many cans is required to paint the wall?

import math

def paint_calc(height, width, coverage):
    area = int(height) * int(width)
    #cover = round( area /cover )
    total_cans = math.ceil( area/ coverage)
    print(f"You'll need {total_cans} cans of paint to paint the wall.")

h = input('Enter the height: ')
w = input('Enter the width: ')
covr = 5

paint_calc(height=h, width=w, coverage=covr)