import csv
import os
import inflect
from .subjects_model import init_subjects, get_subjects_content, sort_subjects
from .add_subject_model import add_subject_model
from .subject_model import get_subject_qnas

csv_directory = "csv_files"
engine = inflect.engine()
subjects_path = os.path.join(csv_directory, "subjects.csv")
    
def update_subject_model(subject, updated_subject):
  if not updated_subject:
    raise ValueError("--INVALID INPUT: Updated name of subject is empty.")
  
  subjects = get_subjects_content()
  
  if not subject in subjects:
    raise FileNotFoundError(f"--INVALID INPUT: {subject.title()} not found.")
  
  old_subject_path = os.path.join(csv_directory, f"{subject}.csv")
  new_subject_path = os.path.join(csv_directory, f"{updated_subject}.csv")

  subjects.remove(subject)
  old_subject_contents = get_subject_qnas(subject)
  os.remove(subjects_path)
  os.remove(old_subject_path)
  init_subjects()
  
  with open(subjects_path, "a", newline="") as subjects_file:
    writer = csv.DictWriter(subjects_file, fieldnames=["subject"])
    for subject in sorted(subjects):
      writer.writerow({ "subject": subject })
      
  add_subject_model(updated_subject)
  
  with open(new_subject_path, "a", newline="") as new_subject:
    new_subject_writer = csv.DictWriter(new_subject, fieldnames=["question", "answer"])
    for content in old_subject_contents:
      new_subject_writer.writerow({ "question": content["question"], "answer": content["answer"] })
  
  sort_subjects()


