from controllers.subject_controller import add_subject_controller
from ..components import border
from ..sleep import delay

def add_subject():
    border()
    try:
        item = input("What subject you'd like to add? ").strip().lower()
        add_subject_controller(item)
    except EOFError:
        return
    except (FileExistsError, ValueError) as e:
        border()
        print(e)
        delay()
    else:
        border()
        print(f"{item.title()} added succesfully.")
        delay()