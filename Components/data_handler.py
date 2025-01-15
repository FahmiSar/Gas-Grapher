from Components.constants import DATA_FILE
import csv

def load_data():
    '''Opens the file and returns a list of the 3 columns in data file'''
    try:
        with open(DATA_FILE, "r") as file:
            reader = csv.reader(file)
            data = [row for row in reader]

        # index 0 is the headers from the CSV so we want everything starting from the first data row
        rows = data[1:]

        dates = []
        amounts = []
        prices = []
        for row in rows:
            dates.append(row[0])
            amounts.append(float(row[1]))
            prices.append(float(row[2]))

        return dates, amounts, prices
    except Exception as e:
        print(f"Error: {e}")