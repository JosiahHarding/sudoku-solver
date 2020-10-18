import math
import constants as c


# This function validates that the size of the board we are using is a perfect square.
# If it is a negative number it should use the absolute value.
# if it is not a square it should use the next perfect square under the number.
def validate_size(size):
    # We need to validate that the size we are using is a perfect square
    root = math.sqrt(abs(size))
    return int(root) ** 2


# here I am creating the board in which I will be using throughout my program
def setup_board():
    board = {}
    for x in range(c.SIZE):
        for y in range(c.SIZE):
            board[(x, y)] = set(range(1, c.SIZE + 1))
    return board


# here I have 2 functions which will be used to isolate column slices in my board,
# using the same code but returning different areas of the code.
def get_col(board, point):
    return get_col_for_id(board, point[0])


def get_col_for_id(board, id):
    slice = {}
    for y in range(c.SIZE):
        p = (id, y)
        slice[p] = board[p]
    return slice


# this is the same as the previous 2 functions, but directed towards rows instead of columns.
def get_row(board, point):
    return get_row_for_id(board, point[1])


def get_row_for_id(board, id):
    slice = {}
    for x in range(c.SIZE):
        p = (x, id)
        slice[p] = board[p]
    return slice


# here I am finding which coordinate goes into which square before getting the slice,
# using the equation a + c.SIDE (refer to constants.py) * d.
def get_sqr_id(point):
    x = point[0]
    y = point[1]
    a = int(x / c.SIDE)
    d = int(y / c.SIDE)
    id = a + c.SIDE * d
    return id


# These two functions are like row and col, but need equations to collect the slice.
def get_sqr(board, point):
    id = get_sqr_id(point)
    return get_sqr_for_id(board, id)


def get_sqr_for_id(board, id):
    slice = {}
    d = int(id / c.SIDE)
    a = id % c.SIDE
    px = a * c.SIDE
    py = d * c.SIDE
    for x in range(c.SIDE):
        for y in range(c.SIDE):
            p = (px + x, py + y)
            slice[p] = board[p]
    return slice


# this function gives the board an appearance that the user can see.
def visualise_board(board):
    output = ""
    for y in range(c.SIZE):
        line = ""
        if y % c.SIDE == 0 and y != 0:
            output += " ---------------------\n"
        for x in range(c.SIZE):
            if x % c.SIDE == 0 and x != 0:
                line += " |"
            if len(board[(x, y)]) == 1:
                line += " " + str(list(board[x, y])[0])
            else:
                line += " ."
        output += line + "\n"
    return output


# this function scans each item in the board for values, making them set values.
def parse_board(sample):
    board = setup_board()
    lines = sample.strip().split("\n")
    y = 0
    for line in lines:
        if "-" in line:
            continue
        x = 0
        values = line.strip().split()
        for value in values:
            if value == "|":
                continue
            if value.isnumeric():
                board[(x, y)] = {int(value)}
            x += 1
        y += 1
    return board


# this funcion will take a board that has had some points set to known values
# it will return a set of the x,y tuples that refer to the points that have been set
# for example: {(0,0),(1,5),(4,2),(7,6)}
def provided_points(board):
    provided = set()
    for p in board.keys():
        if len(board[p]) == 1:
            provided.add(p)
    return provided


def validate_slice(slice):
    expected = list(range(1, c.SIZE + 1))
    actual = []
    for p in slice.keys():
        v = list(slice[p])[0]
        actual.append(v)
    actual.sort()
    return actual == expected


def validate_board(board):
    # here I am ensuring that every set has one possible number.
    for p in board.keys():
        if len(board[p]) != 1:
            return False
    # here I am ensuring all slices contain one of every number.
    of_the_jedi = True
    for id in range(c.SIZE):
        of_the_jedi &= validate_slice(get_row_for_id(board, id))
        of_the_jedi &= validate_slice(get_col_for_id(board, id))
        of_the_jedi &= validate_slice(get_sqr_for_id(board, id))
    return of_the_jedi


def get_message(solved):
    if solved:
        return "I solved it!"
    else:
        return "Gosh Darnit!"


def passing_dict(dict1):
    # I am creating a new blank dict
    dict2 = {}
    # here I am saying for x and y in the original dict,
    # y equals x and insert the new key and value into the 2nd dict
    for x, y in dict1.items():
        dict2[y] = x
    # and lastly, print the second dict.
    return dict2


def dict_manipulation(line):
    cn = {}
    for key, set_of_values in line.items():
        for value in set_of_values:
            if value not in cn.keys():
                cn[value] = set()
            cn[value].add(key)
    return cn
# this will collect all columns that intersect the square being tested.
# returns a list of 3 slices, one for each column.
def get_cols_for_sqr(board, sqr):
    cols = []
    for x, y in sqr.keys():
        col = get_col_for_id(board, x)
        if col not in cols:
            cols.append(col)
    return cols


def get_rows_for_sqr(board, sqr):
    rows = []
    for x, y in sqr.keys():
        row = get_row_for_id(board, y)
        if row not in rows:
            rows.append(row)
    return rows


def find_slice_intersection(slice1, slice2):
    discard = set()
    intersect = set()
    for point in slice1.keys():
        discard.add(point)
    for point in slice2.keys():
        if point in discard:
            intersect.add(point)
    return intersect


