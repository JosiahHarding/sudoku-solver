import setup.initialise as initialise
from . import rules


def test_naked_actual_numbers_rule():
    board = initialise.setup_board()
    board[(0, 8)] = {1}
    naked = initialise.get_col(board, (0, 8))
    updated = rules.actual_numbers_rule(naked)
    for y in range(8):
        assert 1 not in board[(0, y)]
        assert (0, y) in updated

    assert 1 in board[(0, 8)]
    assert (0, 8) not in updated


def test_hidden_actual_numbers_rule():
    board = initialise.setup_board()
    for y in range(8):
        board[(0, y)] = set(range(1, 9))

    hidden = initialise.get_col(board, (0, 8))
    updated = rules.actual_numbers_rule(hidden)
    assert updated == {(0, 8)}
    assert board[(0, 8)] == {9}

def test_multiples_sort():
    board = initialise.setup_board()
    slice = initialise.get_col(board, (0, 0))
    slice[0, 4] = {1, 2, 3}
    sorted = rules.multiples_sort(slice)
    assert sorted[0] == (3, {1, 2, 3}, (0, 4))

def test_find_multiples():
    board = initialise.setup_board()
    slice = initialise.get_col(board, (0, 0))
    slice[0, 4] = {1, 2}
    slice[0, 5] = {1, 2}
    multiples = rules.find_multiples(slice)
    assert len(multiples) == 1
    assert multiples[0] == ({(0, 4), (0, 5)}, {1, 2})

def test_naked_multiples_rule():
    board = initialise.setup_board()
    slice = initialise.get_col(board, (0, 0))
    slice[0, 7] = {1, 2}
    slice[0, 8] = {1, 2}
    updated = rules.multiples_rule(slice)
    assert len(updated) == 7
    for y in range(7):
        assert (0, y) in updated
        assert 1 not in slice[(0, y)]
        assert 2 not in slice[(0, y)]
        assert 1 not in board[(0, y)]
        assert 2 not in board[(0, y)]

def test_hidden_multiples_rule():
    board = initialise.setup_board()
    slice = initialise.get_col(board, (0, 0))
    for y in range(7):
        slice[0, y] = set(range(3, 10))
        board[(0, y)] = slice[(0, y)]

    slice[0, 7] = {1, 2, 3}
    slice[0, 8] = {1, 2, 4}

    for y in range(9):
        board[(0, y)] = slice[(0, y)]

    updated = rules.multiples_rule(slice)
    assert updated == {(0, 7), (0, 8)}
    assert slice[(0, 7)] == {1, 2}
    assert slice[(0, 8)] == {1, 2}
    assert board[(0, 7)] == {1, 2}
    assert board[(0, 8)] == {1, 2}





