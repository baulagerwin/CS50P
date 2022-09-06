import sys


def main():
    lines = []
    count = 0
    
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                for text in file:
                    lines.append(text.rstrip())
                    
                for line in lines:
                    if line.startswith("#") or len(line) == 0:
                        continue
                    count += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
    
    print(count)
main()