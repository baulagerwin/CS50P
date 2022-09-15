from .subjects_model import get_subjects_content

def search_subject_model(subject):
  subjects = get_subjects_content()
  
  if not subject in subjects:
    raise FileNotFoundError(f"--INVALID INPUT: {subject.title()} not found.")