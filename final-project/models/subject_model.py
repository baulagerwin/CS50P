import csv
import os
import inflect

csv_directory = "csv_files"
engine = inflect.engine()
subjects_path = os.path.join(csv_directory, "subjects.csv")

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
  subject_path = os.path.join(csv_directory, f"{subject}.csv")
  
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
    
def search_subject_model(subject):
  subject_path = os.path.join(csv_directory, f"{subject}.csv")
  subjects = []
  questions_and_answers = []
  
  with open(subjects_path) as subjects_file:
    subjects_reader = csv.DictReader(subjects_file)
    for row in subjects_reader:
      subjects.append(row["subject"])
      
    if subject in subjects:
      with open(subject_path) as subject_file:
        subject_reader = csv.DictReader(subject_file)
        for row in subject_reader:
          questions_and_answers.append({ "question": row["question"], "answer": row["answer"] })
        return questions_and_answers
    else:
      raise FileNotFoundError("Subject not found.")
    
def update_subject_model(subject, updated_subject):
  subjects = []
  old_subject_contents = []
  old_subject_path = os.path.join(csv_directory, f"{subject}.csv")
  new_subject_path = os.path.join(csv_directory, f"{updated_subject}.csv")
  
      
  if subject in subjects:
    with open(subjects_path) as subjects_file:
      subjects_reader = csv.DictReader(subjects_file)
      for row in subjects_reader:
        subjects.append(row["subject"])
        
    subjects.remove(subject)
    
    with open(old_subject_path) as old_subject:
      old_subject_reader = csv.DictReader(old_subject)
      for row in old_subject_reader:
        old_subject_contents.append({ "question": row["question"], "answer": row["answer"] })
    
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
      
  else:
    raise FileNotFoundError("Subject not found.")
      
# Create a function for sorting the subjects