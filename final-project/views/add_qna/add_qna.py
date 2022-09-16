from models.add_qna_model import add_qna_model
from ..components import border
from ..sleep import delay

def add_qna(subject):
  border()
  try:
      question = input("Q: ").strip().lower()
      answer = input("A: ").strip().lower()
      
      qna = {
        "question": question,
        "answer": answer
      }
      
      add_qna_model(subject, qna)
  except EOFError:
      return
  except ValueError as e:
      border()
      print(e)
      delay()
  else:
      border()
      print(f"Q & A added succesfully.")
      delay()