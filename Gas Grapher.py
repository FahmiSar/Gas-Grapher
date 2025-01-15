from constants import *
from event_handlers import *

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

def clear_window():
    '''Deletes everything which clears the window'''
    for widget in root.winfo_children():
        widget.destroy()

def make_graph():
    '''Create the graph'''
    global graph_shown

    dates, amounts, prices = load_data()

    plt.figure(figsize=(10,6))
    plt.plot(dates,amounts)

    # Formatting
    plt.xlabel("Date of purchase")
    plt.ylabel("Amount of fuel in Liters")

    # this changes the amount of decimal places
    plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter("%.3f"))

    plt.title("How much fuel I get for $50")
    plt.grid(True)

    # prevents clipping of x-axis labels --> more useful if i include the rotated x labels which i might
    plt.tight_layout()
    
    graph_shown = True


def save_graph(fileName=GRAPH_NAME):
    '''Saves a graph in PNG format and displays it'''
    global graph_shown

    if not graph_shown:
        make_graph()

        # connect the close event to the on_close function to reset the flag
        plt.gcf().canvas.mpl_connect("close_event", on_close)
        
        print("Made graph")

    # this just shows the plot figure but maybe it might be better to just open the file created
    plt.savefig(GRAPH_NAME, dpi=300, bbox_inches="tight")
    plt.show()
    print("Saved and displayed graph")


def submit_data():
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

    # do main_window() => return to main menu after 2000 ms (2 seconds)
    root.after(2000, main_window)

def add_new_entry():
    '''Allows the user to enter a new data entry and saves it to the csv'''
    global entry_widgets

    clear_window()

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
        command=main_window,
        anchor="center"
    ).grid(
        row=2, column=0,
        pady=VERTICAL_PADDING
    )

    # Submit button because I dunno if there's a way to make the Enter key submit
    tk.Button(
        root,
        text="Submit",
        command=submit_data,
        anchor="center"
    ).grid(
        row=2, column=1,
        pady=VERTICAL_PADDING
    )

def main_window():   
    clear_window()

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
              command=add_new_entry,
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


if __name__ == "__main__":
    # this is the main window where everything gets added too
    root = tk.Tk()
    root.title("Gas Grapher")

    # this sets the size of the main window by default (width x height) measured in pixels
    # the other two are shifting the widows position 500 pixels on the X-axis and 300 pixels on the Y-axis 
    root.geometry("400x300+500+300") 

    main_window()