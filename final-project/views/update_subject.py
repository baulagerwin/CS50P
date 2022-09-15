from .components import border
from controllers.subject_controller import update_subject_controller
from .sleep import delay

def update_subject():
    border()
    subject = input("What you'd like to update? ").strip().lower()
    updated_subject = input("What is the name of updated subject? ").strip().lower()
    try:
        update_subject_controller(subject, updated_subject)
    except FileNotFoundError as e:
        border()
        print(e)
        delay()
    else:
        border()
        print("Updated sucessfully!")
        delay()