from ..components import border
from controllers.subject_controller import add_subjects_controller
import inflect
from ..sleep import delay

engine = inflect.engine()

def add_multiple_subjects():
    things = []
    
    border()
    print("Type the subjects below:")
    while True:
        try:
            item = input().strip().lower()
                        
            if item not in things:
                things.append(item)
            else:
                raise ValueError()
        except ValueError as error_message:
            print(error_message)
        except KeyError:
            pass
        except EOFError:
            things = sorted(things)
            break
    
    try:
        subjects = add_subjects_controller(things)
    except FileExistsError as e:
        border()
        print(e)
        delay()
    else:
        border()
        print(f"{engine.join(subjects).capitalize()} are added successfully!")
        delay()