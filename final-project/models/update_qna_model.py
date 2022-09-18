import os
import csv

from .subject_model import get_subject_qnas

def update_qna_model(subject, id, qna):
  if not subject:
    raise ValueError("--INVALID INPUT: Subject name is empty.")
  
  if not id.isdigit():
    raise ValueError("--INVALID INPUT: ID is not a number.")
  
  if not qna["question"] and not qna["answer"]:
    raise ValueError("--INVALID INPUT: Question and answer is empty.")
  
  if not qna["question"]:
    raise ValueError("--INVALID INPUT: Question is empty.")
  
  if not qna["answer"]:
    raise ValueError("--INVALID INPUT: Answer is empty.")
    
  csv_directory = "csv_files"
  subject_path = os.path.join(csv_directory, f"{subject}.csv")
  
  qnas = get_subject_qnas(subject)
  
  id = int(id)
  
  if id <= 0 or id > len(qnas):
    raise ValueError("--INVALID INPUT: ID out of range.")
  
  real_id = id - 1
  
  qnas.pop(real_id)
  qnas.append(qna)
  os.remove(subject_path)
  
  with open(subject_path, "w", newline="") as qnas_file:
    qnas_writer = csv.DictWriter(qnas_file, fieldnames=["question", "answer"])
    qnas_writer.writeheader()
    for qna in sorted(qnas, key=lambda d: d["question"]):
      qnas_writer.writerow({ "question": qna["question"], "answer": qna["answer"]})