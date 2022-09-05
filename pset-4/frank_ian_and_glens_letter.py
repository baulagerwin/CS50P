from random import randint
import sys
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    figlets = ["acrobatic", "alphabet", "big", "madrid", "morse"]
    random_index = randint(0, 4)
    
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):        
        figlet.setFont(font=f"{sys.argv[2]}")
        text = input("Input: ")
        print(figlet.renderText(text))
        
    elif len(sys.argv) == 1:
        figlet.setFont(font=f"{figlets[random_index]}")
        text = input("Input: ")
        print(figlet.renderText(text))
        
    else:
        sys.exit("Invalid command line arguments")
    
main()