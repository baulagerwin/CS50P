from .components import border
from controllers.subject_controller import view_subjects_controller

def view_subjects():
    border()
    subjects = view_subjects_controller()
    
    if len(subjects):
        print("Current subjects are the following: ")
        for i, subject in enumerate(subjects):
            print(f"{i + 1}. {subject.title()}")
    else:
        print("WOW! So empty!")
    
    try:
        print()
        input("Press enter to go back")
    except EOFError:
        return