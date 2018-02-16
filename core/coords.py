class Coords:
    def __init__(self, x=0, y=0):
        self._coords = x, y

    def get_coords(self):
        return self._coords

    def get_row_number(self):
        return self._coords[0]

    def get_col_number(self):
        return self._coords[1]
