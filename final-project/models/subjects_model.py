import csv
import os

csv_directory = "csv_files"
subjects_path = os.path.join(csv_directory, "subjects.csv")

def init_subjects():
  if os.path.exists(subjects_path):
    return
  
  with open(subjects_path, "w", newline="") as subjects_file:
    subjects_writer = csv.DictWriter(subjects_file, fieldnames=["subject"])
    subjects_writer.writeheader()
    
def sort_subjects():
  subjects = get_subjects_content()
  
  os.remove(subjects_path)
  init_subjects()
  
  with open(subjects_path, "a", newline="") as subjects_file:
      writer = csv.DictWriter(subjects_file, fieldnames=["subject"])
      for subject in sorted(subjects):
        writer.writerow({ "subject": subject })
  
def get_subjects_content():
  contents = []
  
  with open(subjects_path) as file:
      reader = csv.DictReader(file)
      for row in reader:
        contents.append(row["subject"])
        
  return contents