# graph_handler.py

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from Components.data_handler import load_data
from Components.constants import GRAPH_NAME

# Flags
graph_shown = False


# pyplot figure close event
def on_close(event):
    global graph_shown
    print("Graph window closed.")
    graph_shown = False


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


def save_graph():
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