import csv
import os
import inflect

engine = inflect.engine()
subjects_path = os.path.join("csv_files", "subjects.csv")

def init_subjects():
  
  try:
    with open(subjects_path, "x") as specific_subject:
     pass
  except (FileExistsError):
    return
  
  with open(subjects_path, "w", newline="") as subjects_file:
    subjects_writer = csv.DictWriter(subjects_file, fieldnames=["subject"])
    subjects_writer.writeheader()

def add_subject_model(subject):
  subject_path = os.path.join("csv_files", f"{subject}.csv")
  
  try:
    with open(subject_path, "x") as specific_subject:
     pass
  except FileExistsError:
    raise FileExistsError(f"--INVALID INPUT: {subject.title()} already exists")
  
  with open(subject_path, "w", newline="") as subject_file, open(subjects_path, "a", newline="") as subjects_file:
    subject_writer = csv.DictWriter(subject_file, fieldnames=["question", "answer"])
    subject_writer.writeheader()
    
    subjects_writer = csv.DictWriter(subjects_file, fieldnames=["subject"])
    subjects_writer.writerow({ "subject": subject }) 
    
def add_subjects_model(subjects):
  existed_subjects_list = []
  
  for subject in subjects:
    try:
      add_subject_model(subject)
    except FileExistsError:
      existed_subjects_list.append(subject)
      pass
  
  if len(existed_subjects_list):
    raise FileExistsError(f"--INVALID INPUT: {engine.join(existed_subjects_list).capitalize()} already exist")
  else:
    return
    
def view_subjects_model():
  subjects = []

  with open(subjects_path) as subjects_file:
      reader = csv.DictReader(subjects_file)
      for row in reader:
          subjects.append(row["subject"])

  return sorted(subjects)
    
  
  
  