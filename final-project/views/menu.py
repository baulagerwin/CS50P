from re import search, IGNORECASE
import sys

from .choices import todo_menu_subject
from .paraphernalia import border, enumerate_to_do, validate_to_do
from .map_list import search_menu

def main_menu():
    border()
    todos = todo_menu_subject()
    enumerate_to_do("--Main Menu", todos)
    menu = search_menu()
    validate_to_do("What would you like to do? ", menu, "--INVALID INPUT: Type what you'd like to do")
    