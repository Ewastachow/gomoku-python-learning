from core.state import State


class Board:
    def __init__(self, col=7, row=7):
        self._col = col
        self._row = row
        self._board = [[State.E for _ in range(col)] for _ in range(row)]

    def __str__(self):
        result = "\n"
        for x in range(self._row):
            result += " |"
            for y in range(self._col):
                state = self._board[x][y]
                if state == State.O:
                    result += "O"
                elif state == State.X:
                    result += "X"
                else:
                    result += " "
            result += "|\n"
        return result

    def add_cell(self, coords, state):
        self._board[coords.get_row_number()][coords.get_col_number()] = state

    def are_coords_valid(self, coords):
        return coords.get_col_number() <= self._col and coords.get_row_number() <= self._row

    def is_empty(self, coords):
        return self._board[coords[0]][coords[1]] == State.E

    def is_full(self):
        result = True
        for x in range(self._row):
            for y in range(self._col):
                if self._board[x][y] == State.E:
                    result = False
        return result

    def whose_move(self):
        circle = 0
        crose = 0
        for i in self._board:
            for s in i:
                if s == State.O:
                    circle += 1
                elif s == State.X:
                    crose += 1
        return State.X if crose <= circle else State.O
