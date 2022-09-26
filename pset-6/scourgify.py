import csv
import sys

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif not (sys.argv[1].endswith(".csv") or sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")
    else:
        try:
            datas = []
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                for text in reader:
                    last_name, first_name = text["name"].split(", ")
                    datas.append({ "first": first_name, "last": last_name, "house": text["house"] })

            with open(sys.argv[2], "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

                writer.writeheader()
                for data in datas:
                    writer.writerow({"first": data["first"], "last": data["last"], "house": data["house"]})

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
main()