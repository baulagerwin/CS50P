# prompts the user for a date in ####-##-## format
# prints how old they are in minutes rounded to the nearest integer
# USING ENGLISH WORDS instead of numerals
# WITHOUT ANY and between words
# ASSUME that the user was born midnight 00:00:00 on that date
# ASSUME also that the current time is in midnight
# use datetime.date.today to get today's date
# u're welcome to import built-in libraries
# if the user does not input a date in ####-##-## format exit via sys.exit
# DO NOT RAISE EXCEPTION

from datetime import datetime, date, time, timedelta
import re
import sys
import inflect

engine = inflect.engine()

def main():
    print(transform(input("Date: ")), "minutes")
    
def transform(s):
    # validate the input
    if match := re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", s):
    
        # if valid -> calculate the total minutes from now
        birth_year = int(match.group("year"))
        birth_month = int(match.group("month"))
        birth_day = int(match.group("day"))
        
        birthday = datetime(birth_year, birth_month, birth_day, 0, 0, 0)
        now_midnight = datetime.combine(date.today(), time(00, 00)) + timedelta(minutes=00)
        duration = (now_midnight - birthday)
        duration_in_minutes = round(duration.total_seconds() / 60)
        
        # convert the result to english words
        words = engine.number_to_words(duration_in_minutes, andword="").capitalize()
        
        # return the result
        return words
    sys.exit("Invalid date format")

if __name__ == "__main__":
    main()