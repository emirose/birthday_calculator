from datetime import date, datetime

today = date.today()
next_year = today.year + 1

def calculate(birthdate):
    results = {}
    birthdate = datetime.strptime(birthdate, '%m/%d/%Y').date()
    next_birthday = calculate_next_birthday(birthdate)
    days_until_next_birthday = (next_birthday - today).days
    results['days_until_next_birthday'] = days_until_next_birthday
    return results

def calculate_next_birthday(birthdate):
    this_years_birthday = birthdate.replace(year=today.year)
    if today > this_years_birthday:
        next_years_birthday = this_years_birthday.replace(year=next_year)
        next_birthday = next_years_birthday
    else:
        next_birthday = this_years_birthday
    return next_birthday


