import sys
import cowsay
from sayings import goodbye

def main():
    
    if len(sys.argv) == 2:
        goodbye(sys.argv[1])
main()