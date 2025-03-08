# ui.py

import tkinter as tk
from tkinter import messagebox
import csv

from Components.constants import *
from Components.graph_handler import save_graph
from Components.data_handler import data_analysis
from Components.utils import *

# Global Variables
entry_widgets = {} # only used for collecting user information from in-app

def submit_data(root):
    '''This extracts and saves user entry into the CSV'''
    global entry_widgets

    # without .items() we iterate over keys which doesn't let us get the value so iterate over values to get both
    # key is the text I've set in the add_new_entry() whereas entry is the tk.Entry object so we use .get() to get the value
    for key,entry in entry_widgets.items():
        # Verifying Date input
        if key == "date":
            userDate = entry.get()
            # exit the function if the date isn't formatted the way we want it
            if not is_valid_date(userDate):
                messagebox.showerror("Error", "Date format is not proper") # error message popup window
                entry.delete(0,tk.END) # this clears the textbox
                return 
            
        if key == "amount":
            userAmount = int(entry.get())
            if not is_valid_amount(userAmount):
                messagebox.showerror("Error", "Amount of fuel is negative or 0")
                entry.delete(0, tk.END)
                return

        if key == "price":
            userPrice = int(entry.get())
            if not is_valid_price(userPrice):
                messagebox.showerror("Error", "Price of fuel is negative")
                entry.delete(0, tk.END)
                return

    
    # Upon a success run the code below
    messagebox.showinfo("Success", "Data Submitted.\nPressing OK will return to the Main Menu")

    # Write data to CSV
    data_to_append = [reformat_date(userDate),userAmount,userPrice]
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(data_to_append)

    # return to main menu - first arguement is time before returning to main menu in ms
    root.after(500, lambda: main_window(root))

def new_entry_window(root):
    '''
        Allows the user to enter a new data entry and saves it to the csv
        ****This creates the window for new data entry
    '''
    global entry_widgets

    clear_window(root)

    # Text explaining fields
    tk.Label(
        root,
        text="Enter the date in MM-DD-YYYY"
    ).grid(
        row=0, column=0,
        pady=VERTICAL_PADDING
    )

    tk.Label(
        root,
        text="Enter the amount of fuel received in Liters"
    ).grid(
        row = 2, column=0,
        pady=VERTICAL_PADDING
    )

    tk.Label(
        root,
        text="Enter the amount paid for fuel in CAD dollars"
    ).grid(
        row = 4, column=0,
        pady=VERTICAL_PADDING
    )

    '''
        I could put these two lines in one jumbo combined line however .grid() returns None since
        all it does is place the widget around so it has no need to return anything this is why we need
        to seperate when we create the widget and when we place it 
    '''
    # text boxes for the user to enter stuff
    date_entry = tk.Entry(root)
    date_entry.grid(row=1, column=0)

    amount_entry = tk.Entry(root)
    amount_entry.grid(row=3, column=0)

    price_entry = tk.Entry(root)
    price_entry.grid(row=5,column=0)

    # add everything to this global array so we can extract info from it later
    # NOTE: this overwrites entries
    entry_widgets["date"] = date_entry
    entry_widgets["amount"] = amount_entry
    entry_widgets["price"] = price_entry 
    

    # Back button to return the user to the main screen
    tk.Button(
        root,
        text="Back",
        command=lambda: main_window(root),
        width=BUTTON_WIDTH,
        anchor="center"
    ).grid(
        row=6, column=0,
        pady=VERTICAL_PADDING
    )

    # Submit button because I dunno if there's a way to make the Enter key submit
    tk.Button(
        root,
        text="Submit",
        command=lambda: submit_data(root),
        width=BUTTON_WIDTH,
        anchor="center"
    ).grid(
        row=6, column=1,
        pady=VERTICAL_PADDING
    )

def data_window(root):
    '''Creates a new window to show stats of the fuel purchased such as:
        how much Fuel per dollar user received, highest and lowest fuel per dollar
    '''

    clear_window(root)

    extreme_pairs, _ = data_analysis()

    # read the data_analysis docstring 
    min_date, min_fuel_ratio = extreme_pairs[0]
    max_date, max_fuel_ratio = extreme_pairs[1]
    
    tk.Label(root,
             text="Fuel Statistics",
             font=(FONT, TITLE_SIZE, "bold")
    ).pack(
        pady=10
    )

    # wraplength limits the label to WINDOW_WIDTH. if it exceeds that it will wrap
    tk.Label(root,
             text=f"On {min_date} you received the lowest amount of fuel per your dollar: {min_fuel_ratio} Liters of fuel per dollar",
             font=(FONT, TEXT_SIZE),
             wraplength=WINDOW_WIDTH,
    ).place(
        relx=0.5, rely=0.3, anchor="center"
    )

    tk.Label(root,
             text=f"On {max_date} you received the highest amount of fuel per your dollar, {max_fuel_ratio} Liters of fuel per dollar",
             font=(FONT, TEXT_SIZE),
             wraplength=WINDOW_WIDTH
    ).place(
        relx=0.5, rely=0.5, anchor="center"
    )


    # return button
    tk.Button(
        root,
        text="Back",
        command=lambda: main_window(root),
        width=BUTTON_WIDTH,
        anchor="center"
    ).place(
        relx=0.1, rely=0.9, anchor="sw"
    )





# ---------------- MAIN MENU -----------------
def main_window(root):   
    clear_window(root)

    # tk.Button(<Stuff>) creates the button that gets added to the main window
    # then <Button>.pack() packs buttons vertically
    # pady is padding in the y-axis (there exists a padx)
    tk.Button(root,
              text="Save Graph",
              command=save_graph,
              width=BUTTON_WIDTH
    ).pack(
        pady=VERTICAL_PADDING,
        anchor="center"
    )
    
    tk.Button(root,
              text="Add new entry",
              command=lambda: new_entry_window(root),
              width=BUTTON_WIDTH
    ).pack(
        pady=VERTICAL_PADDING,
        anchor="center"
    )

    tk.Button(root,
              text="Upload file",
              width=BUTTON_WIDTH
    ).pack(
        pady=VERTICAL_PADDING,
        anchor="center"
    )

    tk.Button(root,
              text="Perform Analysis",
              command=lambda: data_window(root),
              width=BUTTON_WIDTH
    ).pack(
        pady=VERTICAL_PADDING,
        anchor="center"
    )
    
    tk.Button(root,
              text="Exit",
              command=root.destroy, # literally destory the root/main-window to exit the program
              width=BUTTON_WIDTH
    ).pack(
        pady=VERTICAL_PADDING,
        anchor="center"
    )

    # creates a loop that makes tk wait until an event occurs
    root.mainloop()