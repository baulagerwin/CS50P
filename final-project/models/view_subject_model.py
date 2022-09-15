import csv
import os

csv_directory = "csv_files"
subjects_path = os.path.join(csv_directory, "subjects.csv")

def view_subjects_model():
  subjects = []

  with open(subjects_path) as subjects_file:
      reader = csv.DictReader(subjects_file)
      for row in reader:
          subjects.append(row["subject"])

  return sorted(subjects)