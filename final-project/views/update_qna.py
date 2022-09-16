from .view_qna import view_qna
from .components import border
from controllers.subject_controller import update_qna_controller
from .sleep import delay

def update_qna(subject):
  border()
  print("Make sure you view the Q & A of this subject.")
  id = int(input("Choose the number of Q&A you'd like to update: ").strip().lower())
  question = input("Q: ").strip().lower()
  answer = input("A: ").strip().lower()
  
  qna = {
    "question": question,
    "answer": answer
  }
  
  try:
      update_qna_controller(subject, id, qna)
  except ValueError as e:
      border()
      print(e)
      delay()
  else:
      border()
      print("Updated sucessfully!")
      delay()
  