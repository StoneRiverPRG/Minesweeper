""" Minesweeper
Todo: classed
"""

import sys
from enum import Enum, auto
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class GameState(Enum):
    """GameState minesweeper Gaming state

    Args:
        enum ([type]): [description]
    """
    GAME = auto() # playing
    CLEAR = auto() # all mine searched
    BOMB = auto() # mine explosion(Game end)


class Mine():
    """mine minesweeper program.
    Todo:
    """

    def __init__(self):
        self.WIDTH = 30
        self.HEIGHT = 16
        self.MINEMAX = 99
        self.MineCount = self.MINEMAX
        self.MineMap = [[] for _ in range(self.HEIGHT)]
        self.GameState = GameState.GAME
        self.Turn = 0


    def print_Map(self):
        """print_Map display Mine Map
        """
        print(f"turn {self.Turn}", file=sys.stderr)
        for row in self.MineMap:
            print("".join(row), file=sys.stderr)


    def input_data(self):
        # map initialize
        self.MineMap = [[] for _ in range(self.HEIGHT)]

        # map data input
        for i in range(self.HEIGHT):
            for cell in input().split():
                # cell: '?' if unknown, '.' if no mines nearby, '1'-'8' otherwise
                self.MineMap[i].append(cell)


    def update(self):
        pass


    def reveal_cell(self, coord):
        #row, col = coordinate_to_rowcol(coord)
        print("20 7 15 10")



    def coordinate_to_rowcol(self, coord):
        pass


    def main(self):
        while self.GameState == GameState.GAME:
            self.input_data()
            self.update()
            self.print_Map()
            self.reveal_cell((20, 7))
            self.Turn += 1


mine = Mine()
mine.main()