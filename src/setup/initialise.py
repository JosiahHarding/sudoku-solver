import math
import constants as c

# This function validates that the size of the board we are using is a perfect square.
# If it is a negative number it should use the absolute value.
# if it is not a square it should use the next perfect square under the number.
def validate_size(size):
    # We need to validate that the size we are using is a perfect square
    root = math.sqrt(abs(size))
    return int(root) ** 2



def setup_board():
    board = {}
    for x in range(c.SIZE):
        for y in range(c.SIZE):
            board[(x,y)] = set(range(1,c.SIZE+1))
    return board


def get_row(board, point):
    slice = {}
    for y in range(c.SIZE):
        p = (point[0],y)
        slice[p] = board[p]
    return slice


def get_col(board, point):
    slice = {}
    for x in range(c.SIZE):
        p = (x, point[1])
        slice[p] = board[p]
    return slice

# Need to find which coordinate goes into which square, equation is a + c.SIDE * d.
def get_sqr_id(point):
    x = point[0]
    y = point[1]
    a = int(x / c.SIDE)
    d = int(y / c.SIDE)
    id = a + c.SIDE * d
    return id


def get_sqr(board, point):
    slice = {}
    id = get_sqr_id(point)
    d = int(id / 3)
    a = id % 3
    px = a * 3
    py = d * 3
    for x in range(c.SIDE):
        for y in range(c.SIDE):
            p = (px + x, py + y)
            slice[p] = board[p]
    return slice


def print_board(board):
    print()
    print()
    for y in range(c.SIZE):
        line = ""
        if y % c.SIDE == 0 and y != 0:
            print (" ---------------------")
        for x in range(c.SIZE):
            if x % c.SIDE == 0 and x != 0:
                line += " |"
            if len(board[(x, y)]) == 1:
                line += " " + str(list(board[x, y])[0])
            else:
                line += " ."
        print(line)

    return None
