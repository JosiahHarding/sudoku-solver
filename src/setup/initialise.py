import math

def validate_size(size):
    # We need to validate that the size we are using is a perfect square
    root = math.sqrt(abs(size))
    return int(root) ** 2

def get_board(size):
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible = list(range(1, 10))
    # we need to construct the board to use with points and possible values
    return
