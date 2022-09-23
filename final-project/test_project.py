import builtins
import os
from pyfiglet import Figlet

import project

qnas_path = "qnas.csv"

def test_init():
  if not os.path.exists(qnas_path):
    assert os.path.exists(qnas_path) == False
    assert os.path.exists(qnas_path) != True
    
    project.init(qnas_path)
    
    assert os.path.exists(qnas_path) == True
    assert os.path.exists(qnas_path) != False
    
    os.remove(qnas_path)
  else:
    qnas = project.get_qnas(qnas_path)
    os.remove(qnas_path)
    
    assert os.path.exists(qnas_path) == False
    assert os.path.exists(qnas_path) != True
    
    project.init(qnas_path)
    
    assert os.path.exists(qnas_path) == True
    assert os.path.exists(qnas_path) != False
    
    project.write_qnas_back(qnas, qnas_path)

def test_intro(mocker):
  figlet = Figlet()
  figlet.setFont(font="small")
  first_line = figlet.renderText("Welcome to Memforcer")
  second_line = "An application where you can review a subject by generating a random question with their respective answer."
  third_line = "\n"
  
  all_text = first_line + second_line + third_line
  
  spy = mocker.spy(builtins, 'print')
  project.intro()
  spy.assert_called_once_with(all_text)
  
def test_get_started(mocker):
  mocker.patch('builtins.input', return_value="hello")
  assert project.get_started("Press enter to get started...") == "hello"