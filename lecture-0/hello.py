# Create a main function
def main():

    # Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
    name = input("What's your name? ").strip().title()

    # Output using our own function
    hello(name)

    # Output with the default value
    hello()

# Create our own hello function
def hello(to="world"):
    print("hello,", to)
    
# Calls the main function
main()