import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import csv


with open("Data.csv", "r") as file:
    reader = csv.reader(file)
    data = [row for row in reader]


headers = data[0]
rows = data[1:]


dates = []
amounts = []
prices = []
for row in rows:
    dates.append(row[0])
    amounts.append(float(row[1]))
    prices.append(float(row[2]))


plt.figure(figsize=(10,6))
plt.plot(dates,amounts)


# Formatting
plt.xlabel("Date of purchase")
plt.ylabel("Amount of fuel in Liters")

# this changes the amount of decimal places
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter("%.3f"))

plt.title("How much fuel I get for $50")
plt.grid()


plt.savefig("Purchase History.png", dpi=300, bbox_inches="tight")