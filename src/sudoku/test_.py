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
        board[(0, y)] = set(range(1,9))

    hidden = initialise.get_col(board, (0, 8))
    updated = rules.actual_numbers_rule(hidden)
    assert updated == {(0, 8)}
    assert board[(0, 8)] == {9}
