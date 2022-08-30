# defining the main function
def main():
    # reads the input modifies it
    text = convert(input())
    
    # prints the input in lowercase
    print(text)
    
    # defining the convert function
def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")
    
# calling the main function
main()
