from models.add_subject_model import add_subject_model
from models.add_subjects_model import add_subjects_model
from models.view_subject_model import view_subjects_model
from models.update_subject_model import update_subject_model
from models.delete_subject_model import delete_subject_model
from models.search_subject_model import search_subject_model

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
  
def update_subject_controller(subject, updated_subject):
  try:
    update_subject_model(subject, updated_subject)
  except FileNotFoundError as e:
    raise FileNotFoundError(e)
  
def delete_subject_controller(subject):
  try:
    delete_subject_model(subject)
  except FileNotFoundError as e:
    raise FileNotFoundError(e)
  
def search_subject_controller(subject):
  try:
    search_subject_model(subject)
  except FileNotFoundError as e:
    raise FileNotFoundError(e)