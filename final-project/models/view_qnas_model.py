import csv
import os

def view_qnas_model(subject):
  csv_directory = "csv_files"
  subject_path = os.path.join(csv_directory, f"{subject}.csv")
  qnas = []
  
  with open(subject_path) as subject_file:
      reader = csv.DictReader(subject_file)
      for row in reader:
          qnas.append({ "question": row["question"], "answer": row["answer"] })
          
  return sorted(qnas, key=lambda d: d["question"])