import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width = 30
height = 16
mineCount = 99

# game loop
while True:
    for i in range(height):
        for cell in input().split():
            # cell: '?' if unknown, '.' if no mines nearby, '1'-'8' otherwise
            print(cell, file=sys.stderr, end="")
        print("", file=sys.stderr)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print("20 7")
