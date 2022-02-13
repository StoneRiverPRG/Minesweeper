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


class CellState(Enum):
    """CellState cell state
    ?: unopen cell
    .: open clear cell
    1-8: number of mine in neighbor
    S: Safety
    M: Mine
    """
    Q = "?"
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
        # trial code
        self.actions = []
        self.closed_list = []




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


    def find_safety_position(self):
        number_cell = list("12345678")
        neighbor = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for _y, line in enumerate(self.MineMap):
            for _x, s in enumerate(line):
                if s in number_cell:
                    str_dict = self.check_neigbor((_x, _y))
                    if str_dict.get("?") == int(s):
                        # find Mines.
                        for n in neighbor:
                            if self.MineMap[_x+n[0]][_y+n[1]] == "?":
                                self.MineList.append(( _x+n[0], _y+n[1] ))
        # Todo: Needs mine coordinate think



    def check_neigbor(self, coord):
        _x, _y = coord
        neighbor_cell_str = {}
        neighbor = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        for cell in neighbor:
            dx, dy = cell
            x = _x + dx
            y = _y + dy
            if self.check_coordinate((x, y)) == None:
                continue
            s = self.MineMap[x][y]
            if neighbor_cell_str.get(s) == None:
                neighbor_cell_str[s] = 1
            else:
                neighbor_cell_str[s] += 1
        return neighbor_cell_str


    def reveal_cell(self, coord):
        #row, col = coordinate_to_rowcol(coord)
        # TODO:
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
            self.find_safety_position()
            self.print_Map()
            self.reveal_cell((20, 7))
            self.Turn += 1


mine = Mine()
mine.main()