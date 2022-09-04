import inflect

def main():
    engine = inflect.engine()
    names = []
    
    while True:
        try:
            name = input("Name: ")
            names.append(name)
            
        except EOFError:
            break
        
    print(f"Adieu, adieu, to {engine.join(names)}")
main()