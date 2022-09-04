from random import randint


def main():
    
    while True:
        level = int(input("Level: "))
        
        if level >= 0:
            random_number = randint(1, level)
            break
    
    while True:
        number = int(input("Guess: "))
        result = validate_number(random_number, number)
        
        if result.lower() == "just right!":
            print(result)
            break
    
        print(result)
    
def validate_number(number, random_number):
    if number > random_number:
        return "Too small!"
    if number < random_number:
        return "Too large!"
    return "Just right!"
    
main()