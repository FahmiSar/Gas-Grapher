# I dislike having all the imports at the time so for my sanity I wanted to seperate them
# this will also include constants that I may need
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import csv, os, time

# GUI framework
import tkinter as tk
from tkinter import simpledialog, messagebox

# Files 
DATA_FILE = "Data.csv"
GRAPH_NAME = "Purchase History.png"


# Constants
BUTTON_WIDTH = 20
VERTICAL_PADDING = 10
TEXTBOX_WIDTH = 40


# Global Variables
entry_widgets = []


# Flags
graph_shown = False