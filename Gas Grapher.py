from libraries import *


def load_data():
    with open(DATA_FILE, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    # seperate the headers and actual data
    headers = data[0]
    rows = data[1:]

    dates = []
    amounts = []
    prices = []
    for row in rows:
        dates.append(row[0])
        amounts.append(float(row[1]))
        prices.append(float(row[2]))

    return dates, amounts, prices



def make_graph():
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


def on_close(event):
    global graph_shown
    print("Graph window closed.")
    graph_shown = False



def save_graph(fileName=GRAPH_NAME):
    global graph_shown

    if not graph_shown:
        make_graph()

        # connect the close event to the on_close function to reset the flag
        plt.gcf().canvas.mpl_connect("close_event", on_close)
        
        print("Made graph")

    plt.savefig(GRAPH_NAME, dpi=300, bbox_inches="tight")
    plt.show()
    print("Saved and displayed graph")



def main():
    # this is the main window where everything gets added too
    root = tk.Tk()
    root.title("Gas Grapher")

    # this sets the size of the main window by default (width x height) measured in pixels
    root.geometry("400x300") 
    
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
              text="Exit",
              command=root.quit,
              width=BUTTON_WIDTH
    ).pack(
        pady=VERTICAL_PADDING,
        anchor="center"
        )

    # creates a loop that makes tk wait until an event occurs
    root.mainloop()


if __name__ == "__main__":
    main()