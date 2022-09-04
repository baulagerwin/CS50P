import json
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    # print(json.dumps(figlet.getFonts()))
    figlet.setFont(font="o8")
    
    text = input("Input: ")
    print(figlet.renderText(text))
    
main()