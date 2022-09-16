from controllers.subject_controller import delete_qna_controller
from .components import border
from .sleep import delay

def delete_qna(subject):
  border()
  print("Make sure you view the Q & A of this subject.")
  try:
      id = int(input("Choose the number of Q & A you'd like to update: ").strip().lower())
      delete_qna_controller(subject, id)
  except ValueError as e:
      border()
      print(e)
      delay()
  else:
      border()
      print(f"Q & A deleted successfully!")
      delay()