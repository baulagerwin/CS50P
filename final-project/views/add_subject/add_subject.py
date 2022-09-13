from controllers.subject_controller import add_subject_controller
from ..components import border

def add_subject():
    border()
    try:
        item = input("What subject you'd like to add? ").strip().lower()
        add_subject_controller(item)
        return
    except EOFError:
        return
    except FileExistsError as e:
        print(e)
    
    border()