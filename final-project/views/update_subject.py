from .components import border
from controllers.subject_controller import update_subject_controller
from .sleep import delay

def update_subject():
    while True:
        try:
            border()
            subject = input("What you'd like to update? ").strip().lower()
            updated_subject = input("What is the name of updated subject? ").strip().lower()
            update_subject_controller(subject, updated_subject)
        except (FileNotFoundError, ValueError) as e:
            border()
            print(e)
            delay()
        except EOFError:
            return
        else:
            border()
            print("Updated sucessfully!")
            delay()
            return