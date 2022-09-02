def main():
        fuel_gauge = get_fuel_gauge()
        print(fuel_gauge)
    
def get_fuel_gauge():
    while True:
        fuel_gauge = get_fraction("Fraction: ")
        try:
            nume, deno = split_fraction(fuel_gauge)
            percentage = calculate_percentage(nume, deno)
            validated_percentage = validate_percentage(percentage)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return gauge_percentage(validated_percentage)
    
def get_fraction(prompt):
    return input(prompt).strip()
    
def split_fraction(fraction):
    return fraction.split("/")

def calculate_percentage(nume, deno):
    return int((int(nume) / int(deno)) * 100)

def validate_percentage(percentage):
    match percentage:
        case 0 | 25 | 50 | 75 | 100:
            return percentage
        case _:
            # i'm basically sugarcoat throwing an exception here lol :)
            # return calculate_percentage(4, 0)
            raise ValueError
        
def gauge_percentage(percentage):
    match percentage:
        case 0:
            return "E"
        case 25 | 50 | 75: 
            return format_percentage(percentage)
        case 100:
            return "F"
        
def format_percentage(percent):
    return str(percent) + "%"

main()