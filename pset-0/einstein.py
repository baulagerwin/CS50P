def main():
    # reads the input and cast it to int
    mass = int(input("m: "))
    
    # calculates the enery
    energy = calculate_energy(mass)
    
    # prints the energy
    print(f"E: {energy:,}")

def calculate_energy(mass):
    speed_of_light = square(300000000)
    return mass * speed_of_light

def square(number):
    return number * number

main()