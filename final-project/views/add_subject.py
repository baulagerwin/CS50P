def add_subject():
    item = input("Subject: ").strip().lower()
    return item

def add_multiple_subjects():
    things = []
    
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
    
    return things