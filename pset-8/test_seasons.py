# prompts the user for a date in ####-##-## format
# prints how old they are in minutes rounded to the nearest integer
# USING ENGLISH WORDS instead of numerals
# WITHOUT ANY and between words
# ASSUME that the user was born midnight 00:00:00 on that date
# ASSUME also that the current time is in midnight
# use datetime.date.today to get today's date
# u're welcome to import built-in libraries
# if the user does not input a date in ####-##-## format exit via sys.exit
# DO NOT RAISE EXCEPTION

from seasons import transform
import pytest

def test_seasons():
    assert transform("1996-12-12") == "Thirteen million, five hundred thirty-eight thousand, eight hundred eighty"

def test_dash_military():
    with pytest.raises(SystemExit):
        transform("asdf")