import inflect
from .add_subject_model import add_subject_model

engine = inflect.engine()

def add_subjects_model(subjects):
  existed_subjects_list = []
  
  for subject in subjects:
    try:
      add_subject_model(subject)
    except FileExistsError:
      existed_subjects_list.append(subject)
      pass
  
  if len(existed_subjects_list):
    raise FileExistsError(f"--INVALID INPUT: {engine.join(existed_subjects_list).capitalize()} already exists.")
  else:
    return