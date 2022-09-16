from .components import border
from controllers.subject_controller import view_qnas_controller

def view_qna(subject):
  border()
  qnas = view_qnas_controller(subject)
  
  if len(qnas):
      print("Current Q&A's are the following: ")
      for i, qna in enumerate(qnas):
          question = qna["question"]
          answer = qna["answer"]
          print(f"{i + 1}. Q: {question}")
          print(f"   A: {answer}")
  else:
      print("WOW! So empty!")
  
  try:
      border()
      input("Press enter to go back")
  except EOFError:
      return