from ..components import border
from ..sleep import delay
from controllers.subject_controller import add_multiple_qna_controller

def add_multiple_qna(subject):
    things = []
        
    border()
    print("Type the Q & A's below:")
    print()
    count = 1
    while True:
        try:
            question = input(f"Q{count}: ").strip().lower()
            answer = input(f"A{count}: ").strip().lower()
            print()
            
            qna = {
                "question": question,
                "answer": answer
            }
                        
            if qna not in things:
                things.append(qna)
                count += 1
            else:
                raise ValueError()
        except ValueError as error_message:
            print(error_message)
        except KeyError:
            pass
        except EOFError:
            break
    
    try:
        add_multiple_qna_controller(subject, things)
    except ValueError as e:
        border()
        print(e)
        delay()
    else:
        border()
        print("All Q & A are added successfully!")
        print("All questions w/o answers, answers w/o questions, and both empty are skipped!")
        delay()
        return