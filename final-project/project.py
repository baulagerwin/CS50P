import csv
import os
import sys
import time

from re import search, escape
from pyfiglet import Figlet
from random import randint

def main():
  qnas_path = "qnas.csv"
  init(qnas_path)
  intro()
  get_started("Press enter to get started...")
  main_menu(qnas_path)

def init(path):
  if not os.path.exists(path):
    with open_file(path, "w") as file:
      writer = csv_writer(file)
      writer.writeheader()
      
def intro():
  figlet = Figlet()
  figlet.setFont(font="small")
  first_line = figlet.renderText("Welcome to Memforcer")
  second_line = "An application where you can review a subject by generating a random question with their respective answer."
  third_line = "\n"
  
  all_text = first_line + second_line + third_line
  print(all_text)

def get_started(prompt):
  return input(prompt)

def main_menu(path):
  menu_list = get_main_menu_list()
  menu_component("--Main Menu", menu_list, path)

def open_file(path, mode):
  return open(path, mode, newline="")
    
def csv_writer(file_to_write):
  return csv.DictWriter(file_to_write, fieldnames=["question", "answer"])

def csv_reader(file_to_read):
  return csv.DictReader(file_to_read)

def get_qnas(path):
  qnas = []
  
  with open_file(path, "r") as file:
    reader = csv_reader(file)
    
    for row in reader:
      qnas.append({ "question": row["question"], "answer": row["answer"] })

    return qnas

def write_qnas_back(qnas, path):
  with open_file(path, "a") as file:
    writer = csv_writer(file)
    
    for qna in qnas:
      writer.writerow({ "question": qna["question"], "answer": qna["answer"] })

def add_qna_model(qna, qnas_path):
  if not qna["question"] and not qna["answer"]:
    raise ValueError("--INVALID INPUT: Question and answer is empty.")
  elif qna["question"] and not qna["answer"]:
    raise ValueError("--INVALID INPUT: Question without answer.")
  elif not qna["question"] and qna["answer"]:
    raise ValueError("--INVALID INPUT: Answer without question.")
  else:
    with open_file(qnas_path, "a") as file:
      writer = csv_writer(file)
      writer.writerow({ "question": qna["question"], "answer": qna["answer"] })

def add_multiple_qna_model(qnas, path):
  for qna in qnas:
    try:
      if not qna["question"] and not qna["answer"]:
        continue
      if not qna["question"] or not qna["answer"]:
        continue
      
      add_qna_model(qna, path)
    except ValueError as e:
      raise ValueError(e)

def view_qna_model(qnas_path):
  qnas = get_qnas(qnas_path)
  return qnas

def update_qna_model(id, qna, qnas_path):
  qnas = get_qnas(qnas_path)
  
  if not id.isdigit():
    raise ValueError("--INVALID INPUT: ID is not a number.")
  
  if not qna["question"] and not qna["answer"]:
    raise ValueError("--INVALID INPUT: Question and answer is empty.")
  
  if not qna["question"]:
    raise ValueError("--INVALID INPUT: Question is empty.")
  
  if not qna["answer"]:
    raise ValueError("--INVALID INPUT: Answer is empty.")
  
  id = int(id)
  
  if id <= 0 or id > len(qnas):
    raise ValueError("--INVALID INPUT: ID out of range.")
  real_id = id - 1
  qnas = qnas[:real_id]+[qna]+qnas[real_id+1:]
  os.remove(qnas_path)
  init(qnas_path)
  write_qnas_back(qnas, qnas_path)
      
def delete_qna_model(id, qnas_path):
  qnas = get_qnas(qnas_path)
  
  if not id.isdigit():
    raise ValueError("--INVALID INPUT: ID is not a number.")
  
  id = int(id)
  
  if id <= 0 or id > len(qnas):
    raise ValueError("--INVALID INPUT: ID out of range.")
  
  real_id = id - 1
  qnas.pop(real_id)
  os.remove(qnas_path)
  init(qnas_path)
  write_qnas_back(qnas, qnas_path)

def add_qna_controller(qna, qnas_path):
  try:
    add_qna_model(qna, qnas_path)
  except ValueError as e:
    raise ValueError(e)

def add_multiple_qna_controller(qnas, path):
  try:
    add_multiple_qna_model(qnas, path)
  except ValueError as e:
    raise ValueError(e)

def view_qna_controller(qnas_path):
  return view_qna_model(qnas_path)
  
def update_qna_controller(id, qna, qnas_path):
  try:
    update_qna_model(id, qna, qnas_path)
  except ValueError as e:
    raise ValueError(e)
  
def delete_qna_controller(id, qnas_path):
  try:
    delete_qna_model(id, qnas_path)
  except ValueError as e:
    raise ValueError(e)

def border():
  print()
  print("***********************************************")
  print("***********************************************")
  print()

def delay():
  time.sleep(1.5)

def view(qnas):
  print("Current Q & A's are the following: ")
  for i, qna in enumerate(qnas):
      question = qna["question"]
      answer = qna["answer"]
      print(f"{i + 1}. Q: {question}")
      print(f"   A: {answer}")
      print()

def post_view(text):
  border()
  print(text)
  delay()

def exit(path):
  sys.exit()
  
def print_menu(menu_text, menu_list):
  all_text = ""
  border()
      
  for i, todo in enumerate(menu_list):
    mapped = todo["todo"]
    all_text = all_text + f"{i + 1}. {mapped}\n"
    
  print(menu_text)
  print(all_text)

def validate_input(menu_list, todo, path):
  passed_level = 0
  func = ""
  
  """
      First level validation
  """
  for item in menu_list:
    match = item["match"]
    if search(rf".*\b{escape(match)}\b.*", todo):
        passed_level += 1
        break
        
  """
      Second level validation
  """
  for item in menu_list:
    unmatch_count = 0
    for unmatch in item["unmatches"]:
        if search(rf".*\b{escape(unmatch)}\b.*", todo):
            unmatch = 0
            break
        unmatch_count += 1
        
    if unmatch_count == len(item["unmatches"]):
        passed_level += 1
        func = item["function"]
        break
        
  if passed_level == 2:
    func(path)
  else:
    raise ValueError("--INVALID INPUT: Type what would you like to do.")

def throw_random_qna(qnas, number_of_questions):
  border()
  print("Try to answer the random questions below. Press \"enter\" if you like to see the answer.")
  for index in range(int(number_of_questions)):
    random_index = randint(0, len(qnas) - 1)
    random_question = qnas[random_index]["question"]
    answer = qnas[random_index]["answer"]
    input(f"{index + 1}. Q: {random_question} ")
    print(f"   A: {answer}")
    print()
    qnas.pop(random_index)
  border()
  
def menu_component(menu_text, menu_list, path):
  while True:
    try:
      print_menu(menu_text, menu_list)
      print()
      todo = input("What would you like to do? ").strip().lower()
      validate_input(menu_list, todo, path)
    except ValueError as error_message:
      post_view(error_message)
    except EOFError:
      return
  
def review_qna_view(path):
  while True:
    try:
      border()
      qnas = get_qnas(path)
      number_of_questions = input("How many questions you want? ").strip()
      
      if not number_of_questions.isdigit():
          raise ValueError(f"--INVALID INPUT: Number of questions should be a number.")
      elif int(number_of_questions) > len(qnas):
          raise ValueError(f"--INVALID INPUT: Number of questions is greater than the number of questions we have. The current number of question is {len(qnas)}")
      else:
          break
    except ValueError as e:
      post_view(e)
      pass
    except EOFError:
      post_view("Going back.")
      return
    
  throw_random_qna(qnas, number_of_questions)
  input("Press enter to go back.")
  return

def add_qna_view(path):
  while True:
    try:
        border()
        question = input("Q: ").strip()
        answer = input("A: ").strip()
        
        qna = {
          "question": question,
          "answer": answer
        }
        
        add_qna_controller(qna, path)
    except EOFError:
        post_view("Going back.")
        return
    except ValueError as e:
        post_view(e)
        return
    else:
        post_view("Q & A added succesfully.")
        return

def add_multiple_qna_view(path):
  qnas = []
        
  border()
  print("Type the Q & A's below:")
  print()
  count = 1
  while True:
    try:
      question = input(f"Q{count}: ").strip()
      answer = input(f"A{count}: ").strip()
      print()
      
      qna = {
          "question": question,
          "answer": answer
      }
                  
      qnas.append(qna)
      count += 1
    except ValueError as error_message:
      print(error_message)
    except KeyError:
      pass
    except EOFError:
      break
  
  try:
    add_multiple_qna_controller(qnas, path)
  except ValueError as e:
    post_view(e)
    return
  else:
    post_view("All questions w/o answers, answers w/o questions, and both empty are skipped!")
    return

def view_qna_view(path):
  try:
    border()
    qnas = view_qna_controller(path)
    view(qnas) if len(qnas) else print("WOW! So empty! Add Q & A to this subject first.")
    border()
    input("Press enter to go back")
  except EOFError:
    return
  else:
    return

def update_qna_view(path):
  while True:
    try:
      border()
      qnas = view_qna_controller(path)
      
      if len(qnas):
        view(qnas)
        
        border()
        id = input("Choose the number of Q & A you'd like to update: ").strip()
        question = input("Q: ").strip()
        answer = input("A: ").strip()
        
        qna = {
          "question": question,
          "answer": answer
        }
        
        update_qna_controller(id, qna, path)
      else:
          post_view("WOW! So empty! Add Q & A to this subject first.")
          return
      
    except EOFError:
      post_view("Going back.")
      return
    except ValueError as e:
      post_view(e)
      return
    else:
      post_view("Updated sucessfully!")
      return

def delete_qna_view(path):
  while True:
    try:
      border()
      qnas = view_qna_controller(path)
      
      if len(qnas):
          view(qnas)
      else:
          post_view("WOW! So empty! Add Q & A to this subject first.")
          return
      
      border()
      id = input("Choose the number of Q & A you'd like to delete: ").strip().lower()
      delete_qna_controller(id, path)
    except EOFError:
      post_view("Going back.")
      return
    except ValueError as e:
      post_view(e)
      return
    else:
      post_view("Q & A deleted successfully!")
      return

def get_main_menu_list():
  return [
    {
      "todo": "Review Q & A",
      "match": "review",
      "unmatches": ["add", "view", "update", "delete", "exit"],
      "function": review_qna_view
    },
    {
      "todo": "Add Q & A",
      "match": "add",
      "unmatches": ["review", "view", "update", "delete", "exit"],
      "function": add_menu
    },
    {
      "todo": "View Q & A",
      "match": "view",
      "unmatches": ["review", "add", "update", "delete", "exit"],
      "function": view_qna_view
    },
    {
      "todo": "Update Q & A",
      "match": "update",
      "unmatches": ["review", "add", "view", "delete", "exit"],
      "function": update_qna_view
    },
    {
      "todo": "Delete Q & A",
      "match": "delete",
      "unmatches": ["review", "add", "view", "update", "exit"],
      "function": delete_qna_view
    },
    {
      "todo": "Exit",
      "match": "exit",
      "unmatches": ["add", "view", "update", "delete"],
      "function": exit
    },
  ]
    
def get_add_menu_list():
  return [
    {
      "todo": "Single Q & A",
      "match": "single",
      "unmatches": ["multiple"],
      "function": add_qna_view
    },
    {
      "todo": "Multiple Q & A",
      "match": "multiple",
      "unmatches": ["single"],
      "function": add_multiple_qna_view
    }
  ]

def add_menu(path):
  menu_list = get_add_menu_list()
  menu_component("--Add Menu", menu_list, path)
  
if __name__ == "__main__":
    main()