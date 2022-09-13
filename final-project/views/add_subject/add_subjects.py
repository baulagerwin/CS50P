from ..components import border
from controllers.subject_controller import add_subjects_controller

def add_multiple_subjects():
    things = []
    
    border()
    print("Type the subjects below:")
    while True:
        try:
            item = input().strip().lower()
                        
            if item not in things and item:
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
        add_subjects_controller(things)
    except FileExistsError as e:
        print(e)