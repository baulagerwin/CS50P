from random import randint

def main():
    score = 0
    number_of_questions = 10
    level = get_level("Level: ")
    
    for _ in range(number_of_questions):
        minimum_guess = 3
        first_number = generate_integer(level)
        second_number = generate_integer(level)
        result = first_number + second_number
        
        for j in range(minimum_guess):
            human_index = j + 1
            number = ""
            
            print(f"{first_number} + {second_number} = ", end="") 
             
            try:
                number = int(input())
            except (ValueError, UnboundLocalError):
                pass
            
            if number == result:
                score = score + 1
                break
            
            if human_index == minimum_guess:
                print("EEE")
    
    print(f"Score: {score}/{number_of_questions}")
            
    
def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))
            
            if level >= 1 and level <= 3:
                return level
            
        except ValueError:
            pass

def generate_integer(level):
    match level:
        case 1: return randint(0, 9)
        case 2: return randint(10, 99)
        case 3: return randint(100, 999)

main()