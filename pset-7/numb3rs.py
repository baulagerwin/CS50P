import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    truthy_count = 0
    numbers_count = 4
    
    ip = ip.strip()
    if match := re.search(r"([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", ip):
        for i in range(numbers_count):
            human_index = i + 1
            current_number = int(match.group(human_index))
            if current_number >= 0 and current_number <= 255:
                truthy_count += 1
        return truthy_count == numbers_count
    return False
if __name__ == "__main__":
    main()