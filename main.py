# main.py

import tkinter as tk
from Components.ui import main_window
from Components.constants import WINDOW_HEIGHT, WINDOW_WIDTH


if __name__ == "__main__":
    # this is the main window where everything gets added too
    root = tk.Tk()
    root.title("Gas Grapher")

    # get the dimensions of the user's screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate a position so that the window is centered
    x_position = (screen_width // 2) - (WINDOW_WIDTH // 2)
    y_position = (screen_height // 2) - (WINDOW_HEIGHT // 2)
    
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_position}+{y_position}") 

    main_window(root)