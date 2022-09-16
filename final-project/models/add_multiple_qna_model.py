from .add_qna_model import add_qna_model

def add_multiple_qna_model(subject, list_of_qna):
  for qna in list_of_qna:
    try:
      add_qna_model(subject, qna)
    except ValueError as e:
      raise ValueError(e)