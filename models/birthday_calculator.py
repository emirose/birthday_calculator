from datetime import date, datetime

today = date.today()
next_year = today.year + 1

def calculate(birthdate):
    results = {}
    birthdate = datetime.strptime(birthdate, '%m/%d/%Y').date()
    next_birthday = calculate_next_birthday(birthdate)
    days_until_next_birthday = "Unknown" #TODO
    results['days_until_next_birthday'] = days_until_next_birthday
    return results

def calculate_next_birthday(birthdate):
    # TODO
    # return next birthday
    return


