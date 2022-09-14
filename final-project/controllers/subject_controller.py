from models.subject_model import add_subject_model
from models.subject_model import add_subjects_model
from models.subject_model import view_subjects_model
from models.subject_model import search_subject_model
from models.subject_model import update_subject_model

def add_subject_controller(subject):
  try:
    add_subject_model(subject)
  except FileExistsError as e:
    raise FileExistsError(e)
  
def add_subjects_controller(subjects):
  try:
    add_subjects_model(subjects)
  except FileExistsError as e:
    raise FileExistsError(e)
  
def view_subjects_controller():
  return view_subjects_model()

def search_subject_controller(subject):
  try:
    return search_subject_model(subject)
  except FileNotFoundError as e:
    raise FileNotFoundError(e)
  
def update_subject_controller(subject, updated_subject):
  try:
    update_subject_model(subject, updated_subject)
  except FileNotFoundError as e:
    raise FileNotFoundError(e)