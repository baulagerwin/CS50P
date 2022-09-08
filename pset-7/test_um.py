from um import count

def test_count():
    assert count("hello, um, world,") == 1
    assert count("Um, thanks um, for the um, food") == 3
    assert count("thanks to you") == 0
    assert count("Mum, thanks for the food") == 0
    assert count("Umm, hi I am, um, Gerwin") == 1