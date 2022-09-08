from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") != False
    assert validate("510.510.510.510") != True

    assert validate("255.510.510.510") == False
    assert validate("510.255.510.510") == False
    assert validate("510.510.255.510") == False
    assert validate("510.510.510.255") == False

    assert validate("255.255.510.510") == False
    assert validate("510.255.255.510") == False
    assert validate("510.510.255.255") == False
    assert validate("255.510.510.255") == False

    assert validate("255.255.255.510") == False
    assert validate("510.255.255.255") == False
    assert validate("255.510.255.255") == False
    assert validate("255.255.510.255") == False

    assert validate("cat") == False