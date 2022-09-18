import csv
import os
from .subjects_model import get_subjects_content, init_subjects

csv_directory = "csv_files"
subjects_path = os.path.join(csv_directory, "subjects.csv")

def delete_subject_model(subject):
  if not subject:
    raise ValueError("--INVALID INPUT: Subject name is empty.")
  
  subjects = get_subjects_content()
  
  if not subject in subjects:
    raise FileNotFoundError(f"--INVALID INPUT: {subject.title()} not found.")
  
  subject_path = os.path.join(csv_directory, f"{subject}.csv")
  
  subjects.remove(subject)
  os.remove(subjects_path)
  os.remove(subject_path)
  init_subjects()
  
  with open(subjects_path, "a", newline="") as subjects_file:
    writer = csv.DictWriter(subjects_file, fieldnames=["subject"])
    for subject in sorted(subjects):
      writer.writerow({ "subject": subject })
  