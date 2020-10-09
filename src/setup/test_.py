from . import initialise
import constants as c


# here we can see that we are testing the boundaries of our code.
# This is important in my assignment, as I am creating a Sudoku Solver,
# and must ensure that the program is working with perfect squares.
def test_validate_size():
    assert initialise.validate_size(4) == 4     # squares
    assert initialise.validate_size(9) == 9
    assert initialise.validate_size(16) == 16
    assert initialise.validate_size(15) == 9    # non-squares
    assert initialise.validate_size(16.5) == 16 # not a whole number!
    assert initialise.validate_size(-9) == 9    # negative number
    assert initialise.validate_size(-15) == 9   # negative non-square

def test_setup_board():
   board = initialise.setup_board()

   # validate the points
   assert len(board) == c.SIZE**2
   for x in range(c.SIZE):
       for y in range(c.SIZE):
           assert min(board[(x, y)]) == 1
           assert max(board[(x, y)]) == c.SIZE
           assert len(board[(x, y)]) == c.SIZE

def test_get_col():
    board = initialise.setup_board()
    slice = initialise.get_col(board, (0,3))
    assert len(slice.keys()) == c.SIZE
    for y in range(c.SIZE):
        assert (0,y) in slice.keys()
        assert slice[(0,y)] == board[(0,y)]

def test_get_row():
    board = initialise.setup_board()
    slice = initialise.get_row(board, (0,3))
    assert len(slice.keys()) == c.SIZE
    for x in range(c.SIZE):
        assert (x,3) in slice.keys()
        assert slice[(x,3)] == board[(x,3)]

def test_get_sqr_id():
    assert initialise.get_sqr_id((0,0)) == 0
    assert initialise.get_sqr_id((2,2)) == 0
    assert initialise.get_sqr_id((0,3)) == 3
    assert initialise.get_sqr_id((2,5)) == 3
    assert initialise.get_sqr_id((0,6)) == 6
    assert initialise.get_sqr_id((2,8)) == 6
    assert initialise.get_sqr_id((3,0)) == 1
    assert initialise.get_sqr_id((5,2)) == 1
    assert initialise.get_sqr_id((3,3)) == 4
    assert initialise.get_sqr_id((5,5)) == 4
    assert initialise.get_sqr_id((3,6)) == 7
    assert initialise.get_sqr_id((5,8)) == 7
    assert initialise.get_sqr_id((6,0)) == 2
    assert initialise.get_sqr_id((8,2)) == 2
    assert initialise.get_sqr_id((6,3)) == 5
    assert initialise.get_sqr_id((8,5)) == 5
    assert initialise.get_sqr_id((6,6)) == 8
    assert initialise.get_sqr_id((8,8)) == 8


def test_get_sqr():
    board = initialise.setup_board()
    slice = initialise.get_sqr(board, (0,3))
    assert len(slice.keys()) == c.SIZE
    assert (0,3) in slice.keys()
    assert (1,3) in slice.keys()
    assert (2,3) in slice.keys()
    assert (0,4) in slice.keys()
    assert (1,4) in slice.keys()
    assert (2,4) in slice.keys()
    assert (0,5) in slice.keys()
    assert (1,5) in slice.keys()
    assert (2,5) in slice.keys()
    assert slice[(0,3)] == board[(0,3)]
    assert slice[(0,3)] == board[(1,3)]
    assert slice[(0,3)] == board[(2,3)]
    assert slice[(0,3)] == board[(0,4)]
    assert slice[(0,3)] == board[(1,4)]
    assert slice[(0,3)] == board[(2,4)]
    assert slice[(0,3)] == board[(0,5)]
    assert slice[(0,3)] == board[(1,5)]
    assert slice[(0,3)] == board[(2,5)]

def test_visualise_board():
    board = initialise.setup_board()
    board[(0,0)] = {1}
    board[(1,5)] = {4}
    board[(4,2)] = {8}
    board[(7,6)] = {9}
    output = initialise.visualise_board(board)
    parsed_board = initialise.parse_board(output)
    assert parsed_board == board

def test_parse_board():
    sample = " 1 . . | . . . | . . .\n"
    sample += " . . . | . . . | . . .\n"
    sample += " . . . | . 8 . | . . .\n"
    sample += " ---------------------\n"
    sample += " . . . | . . . | . . .\n"
    sample += " . . . | . . . | . . .\n"
    sample += " . 4 . | . . . | . . .\n"
    sample += " ---------------------\n"
    sample += " . . . | . . . | . 9 .\n"
    sample += " . . . | . . . | . . .\n"
    sample += " . . . | . . . | . . ."
    board = initialise.parse_board(sample)
    assert board[(0,0)] == {1}
    assert board[(1,5)] == {4}
    assert board[(4,2)] == {8}
    assert board[(7,6)] == {9}
    assert board[(5,3)] == set(range(1,c.SIZE + 1))

def test_provided_points():
    board = initialise.setup_board()
    board[(0,0)] = {1}
    board[(1,5)] = {4}
    board[(4,2)] = {8}
    board[(7,6)] = {9}
    provided = initialise.provided_points(board)
    assert provided == {(0,0),(1,5),(4,2),(7,6)}

def test_validate_board():
    board = initialise.setup_board()
    assert initialise.validate_board(board) is False
    sample = " 9 2 6 | 8 7 1 | 4 3 5\n"
    sample += "8 5 1 | 3 4 9 | 2 7 6\n"
    sample += "4 7 3 | 2 5 6 | 9 8 1\n"
    sample += "---------------------\n"
    sample += "6 8 5 | 1 3 2 | 7 4 9\n"
    sample += "7 3 4 | 5 8 8 | 6 1 2\n"
    sample += "2 1 9 | 7 6 4 | 3 5 8\n"
    sample += "---------------------\n"
    sample += "5 6 8 | 4 2 7 | 1 9 3\n"
    sample += "3 4 2 | 9 1 5 | 8 6 7\n"
    sample += "1 9 7 | 6 8 3 | 5 2 4"
    board = initialise.parse_board(sample)
    assert initialise.validate_board(board) is False
    sample = " 9 2 6 | 8 7 1 | 4 3 5\n"
    sample += "8 5 1 | 3 4 9 | 2 7 6\n"
    sample += "4 7 3 | 2 5 6 | 9 8 1\n"
    sample += "---------------------\n"
    sample += "6 8 5 | 1 3 2 | 7 4 9\n"
    sample += "7 3 4 | 5 9 8 | 6 1 2\n"
    sample += "2 1 9 | 7 6 4 | 3 5 8\n"
    sample += "---------------------\n"
    sample += "5 6 8 | 4 2 7 | 1 9 3\n"
    sample += "3 4 2 | 9 1 5 | 8 6 7\n"
    sample += "1 9 7 | 6 8 3 | 5 2 4"
    board = initialise.parse_board(sample)
    assert initialise.validate_board(board) is True

def test_get_message():
    message = initialise.get_message(True)
    assert message == "I solved it!"
    message = initialise.get_message(False)
    assert message == "Gosh Darnit!"

def test_passing_board():
    startingDict = {"A": 1, "B": 2, "C": 3}
    outputDict = initialise.passing_dict(startingDict)
    assert outputDict == {1: "A", 2: "B", 3: "C"}

def test_dict_manipulation():
    startingDict = {"A": {1,2,3}, "B": {3,4,5}}
    outputDict = initialise.dict_manipulation(startingDict)
    assert outputDict == {1: {"A"}, 2: {"A"}, 3: {"A", "B"}, 4: {"B"}, 5: {"B"}}






def scratch1():
    # lists
    possible = list(range(1, 10))
    assert len(possible) == 9
    assert possible[5] == 6

    possible.remove(9)
    assert len(possible) == 8
    assert possible[5] == 6

    # tuples
    # possible = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    t = tuple(range(1, 10))
    assert len(t) == 9

    myString = "\nI'm not sure what your asking me"
    assert len(myString) == 33

    for char in myString:
        print(char)
        count = count + 1

    for char in myString:
        print(char)
        count = count + 1

    assert count == 66

    # dict
    myDict = {"key1": 1, "key2": 2, "key3": 3}
    myDict["key3"] = 4
    assert myDict["key3"] == 4

    # set
    mylist = [1, 3, 1, 3, 2, 3]
    assert len(mylist) == 6
    myset = set(mylist)
    assert len(myset) == 3

    size = 9
    # board {point: possible, point: possible, ...}
    #   -> points (x, y)
    #      -> possible [1-9]
    #
    # getRow(board) -> row
    board = {
        "size": 9,
        "side": 3,
        (0,0): possible.copy(),
        (0,1): [1,2,3,4,5,6,7,9],
        (0,2): [1,2,3,4,5,6,7,9],
        (0,3): [1,2,3,4,5,6,7,9],
        (0,4): [1,2,3,4,5,6,7,9],
        (0,5): [1,2,3,4,5,6,7,9],
        (0,6): [1,2,3,4,5,6,7,9],
        (0,7): [1,2,3,4,5,6,7,9],
        (0,8): [1,2,3,4,5,6,7,9],
        (1,0): [1,2,3,4,5,6,7,9],
        (1,1): [1,2,3,4,5,6,7,9]
    }

    for x in range(9):
        for y in range(9):
            myDict[(x,y)] = possible



def _test_scratch2():
    count = 66
    count = count + 1
    assert count == 67

