from random import randint

def main():
    number_of_questions = 10
    minimum_guess = 3
    score = 0
    level = get_level("Level: ")

    for _ in range(number_of_questions):
        first_number = generate_integer(level)
        second_number = generate_integer(level)
        result = first_number + second_number

        for count in range(minimum_guess):
            try:
                print(f"{first_number} + {second_number} = ", end="")
                answer = int(input())

                if (count + 1) == minimum_guess and answer != result:
                    print(f"{first_number} + {second_number} = {result}")

                if (count + 1) != minimum_guess and answer != result:
                    print("EEE")

                if count < minimum_guess and answer == result:
                    score = score + 1
                    break

            except ValueError:
                print("EEE")
                break

    print(f"Score: {score}")


def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))

            if level < 1 or level > 3:
                raise ValueError()
            return level

        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1: return randint(0, 9)
        case 2: return randint(10, 99)
        case 3: return randint(100, 999)
        case _: return

main()