import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import requests

STRING_CHECK = "NO_PROFILE"
URL_STRING = 'https://apps.runescape.com/runemetrics/profile?user='


# creates the interface that will allow the user to select the input text file
def choose_input():
    file_viewer = tk.Tk()
    file_viewer.withdraw()
    file_viewer.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                           filetypes=[("Text Files", "*.txt")])
    check_availability(file_viewer.filename)

def hide_choose_button():
    button1.grid_remove()

def show_choose_button():
    #button2.grid_remove()
    button1 = tk.Button(root, text="Choose Input File", command=lambda: choose_input())
    button1.grid(row=2, column=40)

def show_cancel_button():
    button2 = tk.Button(root, text='Cancel', command=lambda:show_choose_button())
    button2.grid(row=2, column=40)

def check_availability(input_file):
    input_file = open(input_file, 'r')
    output_file = open("booty.txt", 'w')

    # code that will iterate through the file and check all of the names against RuneMetric's profile search feature
    for names in input_file:
        names = names.strip('\n')
        url = URL_STRING + names

        obj = requests.get(url)

        if len(names) <= 12 and re.match("^[a-zA-Z0-9_]*$", names):
            if STRING_CHECK in obj.text:
                line = "Username " + names + " is available."
                output_file.write(names + '\n')
                lb.insert(END, line)
                lb.update_idletasks()
            else:
                print("Username " + names + " is taken.")
        else:
            print("Username " + names + " is invalid.")

    print("Finished.")
    output_file.close()
    input_file.close()

# tkinter gui
root = Tk()
root.title("Runescape Name Checker V1.0")
root.resizable(width=False, height=False)

lb = tk.Listbox(root, height=10, width=70)
lb.grid(row=1, column=40)

button1 = tk.Button(root, text="Choose Input File", command=lambda: choose_input())
button1.grid(row=2, column=40)

img = PhotoImage(file="rs.png")
panel = tk.Label(root, image=img)
panel.grid(row=0, column=40)

root.bind('<Return>', lambda: choose_input())

root.mainloop()

