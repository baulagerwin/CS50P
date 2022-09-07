from plates import is_valid
    
def test_first_two_characters():
    assert is_valid("458008") == False
    assert is_valid("A58008") == False
    assert is_valid("5A8008") == False
    assert is_valid("AA8808") == True
    
def test_number_of_characters():
    assert is_valid("CSIEJFSASDA") == False
    assert is_valid("C") == False
    
def test_characters_in_the_middle():
    assert is_valid("ECT78N") == False
    assert is_valid("EC88NN") == False
    assert is_valid("EC7NNN") == False
    
def test_first_digit():
    assert is_valid("EC8008") == True
    assert is_valid("EC0999") == False
    assert is_valid("ECN099") == False
    assert is_valid("ECNN09") == False
    assert is_valid("ECBTB0") == False
    
def test_space_periods_and_punctuations():
    assert is_valid("EC.808") == False
    assert is_valid("E C808") == False
    assert is_valid("EC808,") == False