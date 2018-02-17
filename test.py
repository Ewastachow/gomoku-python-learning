from core.board import Board
from core.coords import Coords
from core.state import State

b = Board()
b.add_cell(Coords(2, 2), State.X)
print(b)
