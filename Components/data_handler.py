# data_handler.py

from Components.constants import DATA_FILE
import csv
from datetime import datetime

def load_data():
    '''Opens the file and returns a list of the 3 columns in data file'''
    try:
        with open(DATA_FILE, "r") as file:
            reader = csv.reader(file)
            data = [row for row in reader]

        # index 0 is the headers from the CSV so we want everything starting from the first data row
        rows = data[1:]

        rows.sort(key=lambda x: datetime.strptime(x[0], "%b-%d-%Y"))

        dates = []
        amounts = []
        prices = []
        for row in rows:
            dates.append(row[0])
            amounts.append(float(row[1]))
            prices.append(float(row[2]))
        
        print(f"Information read from CSV are:\n Dates: {dates}\nAmounts: {amounts}\nPrices: {prices}")

        return dates, amounts, prices
    except FileNotFoundError as e:
        print(f"{DATA_FILE} does not exist so creating one...")

        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Amount","Price"])
            placeholder = [0]
            return placeholder, placeholder, placeholder
        
    except Exception as e:
        print(f"Error: {e}")


def data_analysis():
    '''REQUIRES: valid data csv which load_data handles
        RETURNS: 
            extreme_pairs, a list of tuples. First entry is minimum, second is max
            the first entry of tuple is date, second is ratio

            array of all fuel per dollars which does not shrink in size so index it like dates
    '''
    dates, amounts, prices = load_data()

    fuel_per_dollar_list = [round(amount / price,2) for amount, price in zip(amounts, prices)]

    min_fuel = max_fuel = fuel_per_dollar_list[0]
    min_date = max_date = dates[0]

    for ratio,date in zip(fuel_per_dollar_list, dates):
        # doing >= so that if there are multiple days with the same fuel per dollar we choose the most recent
        if min_fuel >= ratio:
            min_fuel = ratio
            min_date = date
        if max_fuel <= ratio:
            max_fuel = ratio
            max_date = date

    extreme_pairs = [(min_date, min_fuel), (max_date, max_fuel)]
    return extreme_pairs, fuel_per_dollar_list