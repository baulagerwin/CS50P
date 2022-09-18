from .components import border
from controllers.subject_controller import delete_subject_controller
from .sleep import delay

def delete_subject():
    while True:
        try:
            border()
            subject = input("What subject you'd like to delete? ").strip().lower()
            delete_subject_controller(subject)
        except EOFError:
            return
        except (FileNotFoundError, ValueError) as e:
            border()
            print(e)
            delay()
        else:
            border()
            print(f"{subject.title()} deleted successfully!")
            delay()
            return
    