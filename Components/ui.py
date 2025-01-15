# ui.py

import tkinter as tk

from Components.constants import BUTTON_WIDTH, VERTICAL_PADDING
from Components.graph_handler import save_graph
from Components.utils import clear_window, is_valid_date

# Global Variables
entry_widgets = {}

def submit_data(root):
    global entry_widgets

    # without .items() we iterate over keys which doesn't let us get the value so iterate over values to get both
    # key is the text I've set in the add_new_entry() whereas entry is the tk.Entry object so we use .get() to get the value
    for key,entry in entry_widgets.items():
        # Verifying Date input
        if key == "date":
            if not is_valid_date(entry.get()):
                date_str = None
                print("Invalid date")
            else:
                date_str = entry.get()
                print(f"date_str is {date_str} with type {type(date_str)}")

    '''
        Leaving this Half-baked because I want to sleep so let me write down and explain what I want from this
        the for loop needs to go over 3 things Date, Amount and Price - match the keys and record the items but I also don't want the for loop
        to be incredibly Bulky

        I want a way to run the Label below without having to have some crazy If statement nor Do I really want some crazy stuff thats going on in the If 
        The only condition for the below Label to be displayed is when we have the 3 items and they're well formatted/Valid that is ALL

        Instead of a dictionary I could run with a tuple or an array with a very specific format? like index 0 being date, 1 being amount, 2 being price 
        as I know widgets will not increase any more than 3 textboxes for entries

    '''
    

    if date_str is not None:
        # Some text to show the entered data was successful
        tk.Label(
            root,
            text="New Entry Created Successfully",
            fg="green",
            anchor="center"
        ).grid(
            row=3, column=0,
            pady=VERTICAL_PADDING
        )


        # return to main menu after 2000 ms (2 seconds)
        root.after(2000, lambda: main_window(root))

def add_new_entry(root):
    '''Allows the user to enter a new data entry and saves it to the csv'''
    global entry_widgets

    clear_window(root)

    tk.Label(
        root,
        text="Enter the date in MM-DD-YYYY"
    ).grid(
        row=0, column=0,
        pady=VERTICAL_PADDING
    )

    '''
        I could put these two lines in one jumbo combined line however .grid() returns None since
        all it does is place the widget around so it has no need to return anything this is why we need
        to seperate when we create the widget and when we place it 
    '''
    date_entry = tk.Entry(root)
    date_entry.grid(row=1, column=0)

    # add everything to this global array so we can extract info from it later
    # NOTE: this overwrites entries
    entry_widgets["date"] = date_entry
    

    # Back button to return the user to the main screen
    tk.Button(
        root,
        text="Back",
        command=lambda: main_window(root),
        anchor="center"
    ).grid(
        row=2, column=0,
        pady=VERTICAL_PADDING
    )

    # Submit button because I dunno if there's a way to make the Enter key submit
    tk.Button(
        root,
        text="Submit",
        command=lambda: submit_data(root),
        anchor="center"
    ).grid(
        row=2, column=1,
        pady=VERTICAL_PADDING
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
              command=lambda: add_new_entry(root),
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