import tkinter as tk

from Components.constants import BUTTON_WIDTH, VERTICAL_PADDING
from Components.graph_handler import save_graph

# Global Variables
entry_widgets = []

def clear_window(root):
    '''Deletes everything which clears the window'''
    for widget in root.winfo_children():
        widget.destroy()


def submit_data(root):
    global entry_widgets
    for entry in entry_widgets:
        print(entry.get())

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

    # flush the list since we submitted the data
    entry_widgets.clear()

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
    entry_widgets.append(date_entry)
    

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