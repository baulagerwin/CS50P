from working import convert
import pytest

# str -> covert -> str
# 12 hour format -> convert -> 24 hour format
# 9 AM to 5 PM -> 09:00 to 17:00
# 9:00 AM to 5:00 PM -> 09:00 to 17:00
# 10 PM to 8 AM -> 10:00 to 08:00
# 10:30 PM to 8:50 AM -> 22:30 to 08:50
# 9:60 AM to 5:60 PM -> ValueError
# 9 AM - 5 PM -> ValueError
# 09:00 AM - 17:00 PM -> ValueError

def test_working():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("5 AM to 12 PM") != "5:00 to 12:00"

def test_exceptions():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_dash_standard():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_dash_military():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_omit_to():
    with pytest.raises(ValueError):
        convert("9 AM 12 PM")

def test_out_of_range():
    with pytest.raises(ValueError):
        convert("22 AM to 45 PM")

def test_out_of_range():
    with pytest.raises(ValueError):
        convert("22 la to 45 Sa")

def test_invalid_str():
    with pytest.raises(ValueError):
        convert("asdfasdf")