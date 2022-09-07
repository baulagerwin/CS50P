from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/4") == 0

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_str():
    with pytest.raises(ValueError):
        convert("asdf")

def test_nume_deno():
    with pytest.raises(ValueError):
        convert("10/3")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")