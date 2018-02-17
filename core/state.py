from enum import Enum


class State(Enum):
    O = 1
    X = 2
    E = 3

def string_state(state):
    if state == State.O:
        return "O"
    elif state == State.X:
        return "X"
    else:
        return " "
