from re import sub
from .components import border
from controllers.subject_controller import search_subject_controller

def search_subject():
    border()
    subject = input("What subject you'd like to search? ").strip().lower()
    
    # found -> create a menu -> crud operation for question and answer
    
    # this is for viewing questions and answers
    while True:
        try:
            results = search_subject_controller(subject)
            
            border()
            
            if len(results):
                print("Questions and its answers")
                for i, result in enumerate(results):
                    question = result["question"]
                    answer = result["answer"]
                    print(f"{i + 1}. {question}")
                    print(f"--{answer}")
            else:
                print("No questions and answer was found.")
            input()
        except FileNotFoundError as e:
            print(e)
        except EOFError:
            break
        