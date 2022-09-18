from random import randint
from controllers.subject_controller import review_subject_controller, view_subjects_controller
from .components import border
from .sleep import delay

def review_subject():
    subjects = view_subjects_controller()
    
    while True:
        try:
            if len(subjects):
                border()
                print("Current subjects are the following: ")
                for i, subject in enumerate(subjects):
                    print(f"{i + 1}. {subject.title()}")
            else:
                border()
                print("WOW! So empty!")
                delay()
                return
            
            border()
            id = input("Type the number of subject you'd like to review: ").strip().lower()
            
            if not id.isdigit():
                raise ValueError("--INVALID INPUT: ID should be a number")
            
            id = int(id)
            qnas = review_subject_controller(id)
            
            if len(qnas) <= 0:
                border()
                print("WOW! So empty! Add Q & A to this subject first.")
                border()
                input("Press enter to go back.")
                return
            
            while True:
                try:
                    border()
                    number_of_questions = input("How many questions you want? ").strip().lower()
                    
                    if not number_of_questions.isdigit():
                        raise ValueError(f"--INVALID INPUT: Number of questions should be a number.")
                    elif int(number_of_questions) > len(qnas):
                        raise ValueError(f"--INVALID INPUT: Number of questions is greater than the number of questions we have. The current number of question is {len(qnas)}")
                    else:
                        break
                except ValueError as e:
                    border()
                    print(e)
                    delay()
                    pass
            
            border()
            print("Try to answer the random questions below. Press \"enter\" if you like to see the answer.")
            for index in range(int(number_of_questions)):
                random_index = randint(0, len(qnas) - 1)
                random_question = qnas[random_index]["question"]
                answer = qnas[random_index]["answer"]
                input(f"{index + 1}. Q: {random_question} ")
                print(f"   A: {answer}")
                print()
                qnas.pop(random_index)
                
            border()
            input("Press enter to go back.")
            return
        except EOFError:
            return
        except ValueError as e:
            border()
            print(e)
            delay()