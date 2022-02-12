""" Minesweeper
Todo: classed
"""

import sys
from enum import Enum, auto
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class GameState(Enum):
    """GameState minesweeper state

    Args:
        enum ([type]): [description]
    """
    GAME = auto() # playing
    CLEAR = auto() # all mine searched
    BOMB = auto() # mine explosion(Game end)


class mine():
    """mine minesweeper program.
    Todo:
    """

    def __init__(self):
        self.WIDTH = 30
        self.HEIGHT = 16
        self.MINEMAX = 99

width = 30
height = 16
mineCount = 99


# game loop
while True:
    mine_map = [[] for _ in range(height)]
    for i in range(height):
        for cell in input().split():
            # cell: '?' if unknown, '.' if no mines nearby, '1'-'8' otherwise
            mine_map[i].append(cell)
            # print(cell, file=sys.stderr, end="")
        # print("", file=sys.stderr)

    for line in mine_map:
        print("".join(line), file=sys.stderr)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print("20 7")
