from . import initialise

def test_validateSize():
    assert initialise.validate_size(4) == 4
    assert initialise.validate_size(9) == 9
    assert initialise.validate_size(16) == 16
    assert initialise.validate_size(15) == 9
    assert initialise.validate_size(16.5) == 16
    assert initialise.validate_size(-9) == 9
    assert initialise.validate_size(-15) == 9
