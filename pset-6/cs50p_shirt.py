import csv
import sys

def main():
    extensions = [".jpg", ".jpeg", ".png"]
    tracker = []
    count_truthy = 0
    period = 0
    
    for argv in sys.argv[1:]:
        for letter in argv:
            if letter == ".":
                period += 1
        
        for extension in extensions:
            tracker.append(argv.endswith(extension))
            
    for boolean in tracker:
        if boolean:
            count_truthy += 1
    
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif period < 2 or period > 2 or count_truthy == 0:
        sys.exit("Invalid input")
    elif sys.argv[1][sys.argv[1].index("."):] != sys.argv[2][sys.argv[2].index("."):]:
        sys.exit("Input and output have different extension")
        
main()