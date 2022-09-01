from curses.ascii import isalpha, isdigit

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (len(s) >= 2 and len(s) <= 6):
        return False
    
    if not (isalpha(s[0:1]) and isalpha(s[1:2])):
        return False
    
    for char in s:
        if not (isalpha(char) or isdigit(char)):
            return False
    
    last_chars = s[2:]
    
    for i in range(len(last_chars)):
        for j in range(len(last_chars)):
            
            # Skip the previous i
            if j <= i:
                continue
            
            # checks if the current char is 0
            if last_chars[i] == "0":
                return False
            
            # checks if the current char is not a digit
            if not isdigit(last_chars[j]):
                return False
                
    return True

main()