""" Minesweeper
Todo:
    classed
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
    """Mine minesweeper program.
    Todo:a
    """

    def __init__(self):
        self.WIDTH = 30
        self.HEIGHT = 16
        self.MINEMAX = 99
        self.MineCount = self.MINEMAX # Current number of Mine.
        self.MineMap = [[] for _ in range(self.HEIGHT)]
        self.GameState = GameState.GAME
        self.Turn = 0
        self.MineList = [] # Coordinate of (row, col) list(tuples) of mine.


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



    def check_coordinate(self, coord):
        """check_coordinate (x, y)coordinate

        Args:
            coord (tuple): (x, y) coordinate

        Returns:
            tuple: (x, y) if check is True, else None
        """
        # *check legal position
        if not len(coord) == 2:
            return
        x, y = coord
        if not ((0 <= x < self.WIDTH) and (0 <= y < self.HEIGHT)):
            # ! if list index is out of range.
            return

        # *: order is x and y. not row and col.
        return (x, y)



    def main(self):
        while self.GameState == GameState.GAME:
            self.input_data()
            self.update()
            self.print_Map()
            self.reveal_cell((20, 7))
            self.Turn += 1


mine = Mine()
mine.main()