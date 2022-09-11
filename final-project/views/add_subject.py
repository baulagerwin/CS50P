from .choices import todo_adding_subject
from .paraphernalia import border, enumerate_to_do

def add_subject():
    border()
    
    todos = todo_adding_subject()
    enumerate_to_do("--Add Menu", todos)
    todo = input("What would you like to do? ")
    
    
def add_item():
    item = input("Item: ").strip().lower()
    return item
    
def add_multiple_items():
    things = []
    
    while True:
        try:
            item = input("Items: ").strip().lower()
                        
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
    
    return things