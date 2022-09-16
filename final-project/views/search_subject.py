from .components import border
from controllers.subject_controller import search_subject_controller
from .sleep import delay
from .search_subject_menu_list import search_subject_menu_list
from .components import menu

def search_subject():
    border()
    subject = input("What subject you'd like to search? ").strip().lower()
    
    try:
        search_subject_controller(subject)
    except FileNotFoundError as e:
        border()
        print(e)
        delay()
    else:
        border()
        search_subject = search_subject_menu_list()
        menu(f"--{subject.title()} Menu", "What would you like to do? ", search_subject, "--INVALID INPUT: Type what you'd like to do.", subject)