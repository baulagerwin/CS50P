import sys
from re import search, escape

def border():
    print()
    print("********************************************")
    print()
    
def enumerate_to_do(menu, todos):
    print(menu)
    for i, todo in enumerate(todos):
        print(f"{i + 1}. {todo}")
    print()
        
def validate_to_do(prompt, map, error_msg):
    while True:
        try:
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
            
            if passed_level == 2:
                func()
            else:
                raise ValueError(error_msg)
                
        except ValueError as error_message:
            print(error_message)
        
def exit():
    sys.exit()