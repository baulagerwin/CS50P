from models.add_subject_model import add_subject_model
from models.add_subjects_model import add_subjects_model
from models.view_subject_model import view_subjects_model
from models.update_subject_model import update_subject_model
from models.delete_subject_model import delete_subject_model
from models.search_subject_model import search_subject_model
from models.add_qna_model import add_qna_model
from models.add_multiple_qna_model import add_multiple_qna_model
from models.view_qnas_model import view_qnas_model
from models.update_qna_model import update_qna_model
from models.delete_qna_model import delete_qna_model

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
  
def add_qna_controller(subject, qna):
  try:
    add_qna_model(subject, qna)
  except ValueError as e:
    raise ValueError(e)
  
def add_multiple_qna_controller(subject, list_of_qna):
  try:
    add_multiple_qna_model(subject, list_of_qna)
  except ValueError as e:
    raise ValueError(e)
  
def view_qna_controller(subject):
  return view_qnas_model(subject)

def update_qna_controller(subject, id, qna):
  try:
    update_qna_model(subject, id, qna)
  except ValueError as e:
    raise ValueError(e)
  
def delete_qna_controller(subject, id):
  try:
    delete_qna_model(subject, id)
  except ValueError as e:
    raise ValueError(e)