from bank import value

def test_right():
    assert value("hello world") == 0
    assert value("how you doing?") == 20
    assert value("what's good?") == 100
    assert value("Hello world") == 0
    assert value("How you doing?") == 20
    assert value("What's good?") == 100

def test_wrong():
    assert value("what's good?") != 0
    assert value("what's good?") != 20

    assert value("how you doing?") != 0
    assert value("how you doing?") != 100

    assert value("hello world") != 20
    assert value("hello world") != 100

    assert value("123") == 100
    assert value(".?!,:;/-}{()'\"") == 100
