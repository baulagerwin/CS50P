from .subject_model import get_subject_qnas
from .subjects_model import get_subjects_content

def review_subject_model(id):
  subjects = get_subjects_content()
  
  if id <= 0 or id > len(subjects):
    raise ValueError("--INVALID INPUT: ID out of range.")
  
  index = id - 1
  subject = subjects[index].lower()
  
  return get_subject_qnas(subject)
  