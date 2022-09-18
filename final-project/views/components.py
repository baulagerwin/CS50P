import sys
from re import search, escape

def border():
    print()
    print("*************************************************************")
    print("*************************************************************")
    print()
    
def exit():
    sys.exit()
    
def go_back_with_arg(subject):
    raise EOFError

def go_back():
    raise EOFError
    
def menu(menu_text, prompt, map, error_msg, prop):
    while True:
        try:
            border()
            
            print(menu_text)
            
            for i, todo in enumerate(map):
                mapped = todo["todo"]
                print(f"{i + 1}. {mapped}")
            print()
            
            todo = input(prompt).strip().lower()
            passed_level = 0
            func = ""
            
            """
                First level validation
            """
            for item in map:
                match = item["match"]
                if search(rf".*\b{escape(match)}\b.*", todo):
                    passed_level += 1
                    break
            
            """
                Second level validation
            """
            for item in map:
                unmatch_count = 0
                for unmatch in item["unmatches"]:
                    if search(rf".*\b{escape(unmatch)}\b.*", todo):
                        unmatch = 0
                        break
                    unmatch_count += 1
                    
                if unmatch_count == len(item["unmatches"]):
                    passed_level += 1
                    func = item["function"]
                    break
            
            if passed_level == 2 and not prop:
                func()
            elif passed_level == 2 and prop:
                func(prop)
            else:
                raise ValueError(error_msg)
                
        except ValueError as error_message:
            border()
            print(error_message)
        except EOFError:
            break
        
