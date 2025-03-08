# utils.py


import re #regular expression
from datetime import datetime

def clear_window(root):
    '''Deletes everything which clears the window'''
    for widget in root.winfo_children():
        widget.destroy()


def is_valid_date(date_str: str) -> bool:
    '''Validates if the input date is in MM-DD-YYYY'''
    date_pattern = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$"
    '''
        ChatGPT helped with this so I'm going to break it down or else I will forget
        ^ $ are the syntax to label beginning and ending of a regex
        0[1-9] | 1[0-2] is so we can have months either as 01 to 09 OR 10 to 12 ==> Months
        0[1-9] | [12][0-9] |3[01] is so we can have days from 01 to 09 (first part) OR the tens digit can be either 1 or 2 and the ones being 0-9 i.e 13, 29 OR we have 30 or 31
        \d{4} legit just 4 digits for the year
    '''
    return bool(re.match(date_pattern, date_str))


def is_valid_amount(amount: int) -> bool:
    '''Validates if amount of fuel is negative or 0'''
    if amount <= 0:
        print(f"Amount of fuel recieved is negative or 0")
        return False
    else:
        return True
    
def is_valid_price(price: int) -> bool:
    '''Validates if price paid for fuel is valid'''
    if price < 0:
        print(f"Price of fuel is negative")
        return False
    else:
        return True


def reformat_date(numeric_date: int) -> str:
    '''Converts numerical version of date into abbreviated version'''
    try:
        # takes an int version of date MM-DD-YYYY
        date_obj = datetime.strptime(str(numeric_date), "%m-%d-%Y")
        
        # converts that int version into Name-Day-Year
        return date_obj.strftime("%b-%d-%Y")
    
    except ValueError as e:
        print(f"Error: {e}")
        return None
    

