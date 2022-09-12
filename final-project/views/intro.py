from pyfiglet import Figlet

from .components import border

def intro():
    figlet = Figlet()
    figlet.setFont(font="small")
    print(figlet.renderText("Welcome to Studious"))
    print("An application where you can review a subject by generating a random question with their respective answer.")
    print()
    input("Press enter to get started...")
    
    border()