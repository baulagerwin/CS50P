from bank import value

def test_bank():
    assert value("hello") == "0"
    assert value("hey what's good?") == "20"
    assert value("what's poppin?") == "100"