from . import initialise

def test_validateSize():
    assert initialise.validateSize(4) == 4
    assert initialise.validateSize(9) == 9
    assert initialise.validateSize(16) == 16
    assert initialise.validateSize(15) == 9
    assert initialise.validateSize(16.5) == 16
    assert initialise.validateSize(-9) == 9
    assert initialise.validateSize(-15) == 9
