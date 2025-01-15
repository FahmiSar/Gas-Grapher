import tkinter as tk
from Components.ui import main_window


if __name__ == "__main__":
    # this is the main window where everything gets added too
    root = tk.Tk()
    root.title("Gas Grapher")

    # this sets the size of the main window by default (width x height) measured in pixels
    # the other two are shifting the widows position 500 pixels on the X-axis and 300 pixels on the Y-axis 
    root.geometry("400x300+500+300") 

    main_window(root)