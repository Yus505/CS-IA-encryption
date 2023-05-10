import tkinter as tk
import random
from tkinter import ttk, simpledialog, messagebox
import pdfkit

# create tkinter window
window = tk.Tk()
window.title("Table with Binary and Hexadecimal Values")

# create table
table_columns = ("Integer", "Binary", "Hexadecimal")
table = ttk.Treeview(window, columns=table_columns, show="headings")
for col in table_columns:
    table.heading(col, text=col.title())
    table.column(col, width=100, anchor="center")
table.pack()

# function to add new row to the table
def add_row():
    integer = int_entry.get()
    binary = bin(integer)[2:]
    hexadecimal = hex(integer)[2:].upper()
    table.insert("", tk.END, values=(integer, binary, hexadecimal))

# create input fields and add row button
int_label = tk.Label(window, text="Integer:")
int_entry = tk.Entry(window)
add_row_button = tk.Button(window, text="Add Row", command=add_row)
int_label.pack()
int_entry.pack()
add_row_button.pack()

# function to convert values
def convert():
    score = 0
    for i in range(10):
        # choose random conversion
        choice = random.choice(["integer to binary", "integer to hexadecimal", "binary to integer", "hexadecimal to integer"])
        # generate random value
        if choice.startswith("integer"):
            value = random.randint(0, 255)
        else:
            value = random.choice(["AA", "BB", "CC", "DD", "EE", "FF"])
        # show conversion prompt and get user input
        if choice == "integer to binary":
            prompt = f"Convert {value} to binary:"
            expected = bin(int(value, 16))[2:].zfill(8)
        elif choice == "integer to hexadecimal":
            prompt = f"Convert {value} to hexadecimal:"
            expected = hex(int(value, 2))[2:].upper()
        elif choice == "binary to integer":
            prompt = f"Convert {value} to decimal:"
            expected = str(int(value, 2))
        elif choice == "hexadecimal to integer":
            prompt = f"Convert {value} to decimal:"
            expected = str(int(value, 16))
        user_input = simpledialog.askstring("Quiz", prompt)
        if user_input == expected:
            score += 1
    messagebox.showinfo("Quiz Result", f"You scored {score} out of 10.")

# create quiz button
quiz_button = tk.Button(window, text="Quiz", command=convert)
quiz_button.pack()

# function to download table as PDF
def download_pdf():
    options = {
        "page-size": "A4",
        "orientation": "landscape"
    }
    pdfkit.from_string(table.to_csv(), "table.pdf", options=options)
    messagebox.showinfo("Download PDF", "Table downloaded as PDF.")

# create download PDF button
download_pdf_button = tk.Button(window, text="Download PDF", command=download_pdf)
download_pdf_button.pack()

# start tkinter event loop
window.mainloop()
