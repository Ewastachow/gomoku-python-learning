from core.state import State


def cell_oposition(state):
    if state == State.X:
        return State.O
    elif state == State.O:
        return State.X
    else:
        return State.E