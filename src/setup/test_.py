from . import initialise


def test_validate_size():
    count = 0
    assert initialise.validate_size(4) == 4
    assert initialise.validate_size(9) == 9
    assert initialise.validate_size(16) == 16
    assert initialise.validate_size(15) == 9
    assert initialise.validate_size(16.5) == 16
    assert initialise.validate_size(-9) == 9
    assert initialise.validate_size(-15) == 9


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



def test_scratch2():
    count = 66
    count = count + 1
    assert count == 67
