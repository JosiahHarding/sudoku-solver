import math

def validate_size(size):
    # We need to validate that the size we are using is a perfect square
    root = math.sqrt(abs(size))
    return int(root) ** 2

def get_board(size):
    # we need to construct the board to use with points and possible values
    return
