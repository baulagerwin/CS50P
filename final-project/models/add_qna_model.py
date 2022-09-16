import csv
import os

def add_qna_model(subject, qna):
  csv_directory = "csv_files"
  subject_path = os.path.join(csv_directory, f"{subject}.csv")
  
  if not qna["question"] and not qna["answer"]:
    return
  elif qna["question"] and not qna["answer"]:
    raise ValueError("--INVALID INPUT: Question without answer.")
  elif not qna["question"] and qna["answer"]:
    raise ValueError("--INVALID INPUT: Answer without question.")
  else:
    with open(subject_path, "a", newline="") as subject_file:
      writer = csv.DictWriter(subject_file, fieldnames=["question", "answer"])
      writer.writerow({ "question": qna["question"], "answer": qna["answer"] })