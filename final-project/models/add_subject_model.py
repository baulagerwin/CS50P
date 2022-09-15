import csv
import os

csv_directory = "csv_files"
subjects_path = os.path.join(csv_directory, "subjects.csv")

def add_subject_model(subject):
  subject_path = os.path.join(csv_directory, f"{subject}.csv")
  
  if os.path.exists(subject_path):
    raise FileExistsError(f"--INVALID INPUT: {subject.title()} already exists")
  
  with open(subject_path, "w", newline="") as subject_file, open(subjects_path, "a", newline="") as subjects_file:
    subject_writer = csv.DictWriter(subject_file, fieldnames=["question", "answer"])
    subject_writer.writeheader()
    
    subjects_writer = csv.DictWriter(subjects_file, fieldnames=["subject"])
    subjects_writer.writerow({ "subject": subject }) 