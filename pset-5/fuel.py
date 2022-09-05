def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            fuel_gauge = gauge(percentage)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            print(fuel_gauge)
            break

def convert(fraction):
    nume, deno = split_and_cast_fraction(fraction)
    
    nume = int(nume)
    deno = int(deno)
    
    if nume > deno:
        raise ValueError
    
    percentage = calculate_percentage(nume, deno)
    return percentage

def gauge(percentage):    
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return format_percentage(percentage)
        
def split_and_cast_fraction(fraction):
    return fraction.split("/")

def calculate_percentage(nume, deno):
    return round((nume / deno) * 100)

def format_percentage(percent):
    return str(percent) + "%"

if __name__ == "__main__":
    main()