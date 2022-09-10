from mock_subjects import get_subjects, get_things_todo
from pyfiglet import Figlet
import re

def main():
    figlet = Figlet()
    figlet.setFont(font="small")
    print(figlet.renderText("Welcome to Studious"))
    print("An application where you can review a subject by generating a random question with their respective answer.")
    print()
    input("Press enter to get started...")
    
    print()
    print("********************************************")
    print()
    
    todos = get_things_todo()
    print("Menu: ")
    for i, todo in enumerate(todos):
        print(f"{i + 1}. {todo}")
    todo = input("What would you like to do? ").strip().lower()
    
    if re.search(r".*\breview\b.*", todo):
        print("Review")

def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
    
    # autopep8
    # subjects = get_subjects()
    # for i, subject in enumerate(subjects):
    #     print(f"{i + 1}. {subject}")
    # input("Choose a subject: ")

    # print()
    # print("********************************************")
    # print()