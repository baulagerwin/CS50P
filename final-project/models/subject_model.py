import csv
import os

csv_directory = "csv_files"

def get_subject_qnas(subject):
  subject_path = os.path.join(csv_directory, f"{subject}.csv")
  qnas = []
  
  with open(subject_path, "r") as file:
      reader = csv.DictReader(file)
      for row in reader:
        qnas.append({ "question": row["question"], "answer": row["answer"] })
        
  return qnas

def sort_qnas(subject):
  subject_path = os.path.join(csv_directory, f"{subject}.csv")
  
  qnas = get_subject_qnas(subject)
  os.remove(subject_path)
  
  with open(subject_path, "w", newline="") as qnas_file:
    qnas_writer = csv.DictWriter(qnas_file, fieldnames=["question", "answer"])
    qnas_writer.writeheader()
    
    for qna in sorted(qnas, key=lambda d: d["question"]):
      qnas_writer.writerow({ "question": qna["question"], "answer": qna["answer"]})