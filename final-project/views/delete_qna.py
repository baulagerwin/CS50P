from controllers.subject_controller import delete_qna_controller, view_qna_controller
from .components import border
from .sleep import delay

def delete_qna(subject):
    while True:
        try:
            border()
            qnas = view_qna_controller(subject)
            
            if len(qnas):
                print("Current Q & A's are the following: ")
                for i, qna in enumerate(qnas):
                    question = qna["question"]
                    answer = qna["answer"]
                    print(f"{i + 1}. Q: {question}")
                    print(f"   A: {answer}")
            else:
                border()
                print("WOW! So empty! Add Q & A to this subject first.")
                delay()
                return
            
            border()
            id = input("Choose the number of Q & A you'd like to delete: ").strip().lower()
            delete_qna_controller(subject, id)

        except EOFError:
            return
        except ValueError as e:
            border()
            print(e)
            delay()
        else:
            border()
            print(f"Q & A deleted successfully!")
            delay()
            return