from .add_qna_menu_list import add_qna_menu_list
from ..components import border, menu
from ..sleep import delay

def add_qna_menu(subject):
  add_qna = add_qna_menu_list()
  menu("--Add Q & A Menu", "Choose one of the above: ", add_qna, "--INVALID INPUT: Type how many you want to add", subject)