import csv
import os

from .subjects_model import sort_subjects

csv_directory = "csv_files"
subjects_path = os.path.join(csv_directory, "subjects.csv")

def add_subject_model(subject):
  if not subject:
    raise ValueError(f"--INVALID INPUT: Subject name is empty")
  
  subject_path = os.path.join(csv_directory, f"{subject}.csv")
  
  if os.path.exists(subject_path):
    raise FileExistsError(f"--INVALID INPUT: {subject.title()} already exists")
  
  with open(subject_path, "w", newline="") as subject_file, open(subjects_path, "a", newline="") as subjects_file:
    subject_writer = csv.DictWriter(subject_file, fieldnames=["question", "answer"])
    subject_writer.writeheader()
    
    subjects_writer = csv.DictWriter(subjects_file, fieldnames=["subject"])
    subjects_writer.writerow({ "subject": subject })
    
  sort_subjects()
  