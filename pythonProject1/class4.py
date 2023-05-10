import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Table with Integers, Binary, and Hexadecimal Values")

        # Create the table
        self.table = Table(self.master, ["Integer", "Binary", "Hexadecimal"])

        # Create the input fields and add button
        self.integer_var = tk.StringVar()
        self.binary_var = tk.StringVar()
        self.hexa_var = tk.StringVar()
        tk.Label(self.master, text="Integer:").pack()
        tk.Entry(self.master, textvariable=self.integer_var).pack(pady=5)
        tk.Label(self.master, text="Binary:").pack()
        tk.Entry(self.master, textvariable=self.binary_var).pack(pady=5)
        tk.Label(self.master, text="Hexadecimal:").pack()
        tk.Entry(self.master, textvariable=self.hexa_var).pack(pady=5)
        tk.Button(self.master, text="Add Row", command=self.add_row).pack(pady=10)

        # Create the Quiz and Download PDF buttons
        tk.Button(self.master, text="Quiz", command=self.quiz).pack(pady=10)
        tk.Button(self.master, text="Download PDF", command=self.download_pdf).pack(pady=10)

    def add_row(self):
        # Add a new row to the table with the inputted values
        integer = self.integer_var.get()
        binary = self.binary_var.get()
        hexa = self.hexa_var.get()

        # Convert the inputted values to binary and hexadecimal
        if integer:
            binary = bin(int(integer))[2:]
            hexa = hex(int(integer))[2:]
        elif binary:
            integer = int(binary, 2)
            hexa = hex(integer)[2:]
        elif hexa:
            integer = int(hexa, 16)
            binary = bin(integer)[2:]

        self.table.add_row(integer, binary, hexa)

    def quiz(self):
        # Quiz the user on converting between binary, decimal, and hexadecimal values
        questions = [("Convert 10101011 from binary to decimal.", "171"),
                     ("Convert 235 from decimal to binary.", "11101011"),
                     ("Convert AFF from hexadecimal to decimal.", "2815"),
                     ("Convert 1000110101 from binary to hexadecimal.", "8D"),
                     ("Convert 352 from decimal to hexadecimal.", "160"),
                     ("Convert 7F from hexadecimal to binary.", "1111111"),
                     ("Convert 10101010 from binary to hexadecimal.", "AA"),
                     ("Convert 257 from decimal to binary.", "100000001"),
                     ("Convert B1 from hexadecimal to decimal.", "177"),
                     ("Convert 11101011 from binary to hexadecimal.", "EB")]

        # Ask the user each question and keep track of the score
        score = 0
        for question, answer in questions:
            user_answer = messagebox.askquestion(f"Question {questions.index((question, answer)) + 1}", question)
            if user_answer == answer:
                score += 1

        # Show the user's final score
        messagebox.showinfo("Quiz Result", f"You scored {score}/{len(questions)}.")

    def download_pdf(self):
        # Create a PDF document and add the table to it
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add the table headers
        for header in self.table.headers:
            pdf.cell(100, 10, header, border=1)

        # Add the table rows
        for row in self.table.table.get_children():
            values = self.table.table.item(row)["values"]
            pdf.ln()
            for value in values:
                pdf.cell(100, 10, str(value), border=1)

        # Save the PDF document
        pdf.output("table.pdf")

class Table:
    def __init__(self, parent, headers):
        self.parent = parent
        self.headers = headers
        self.table = ttk.Treeview(self.parent, columns=self.headers, show="headings")
        self.table.pack(pady=10)

        # Set columns heading and width
        for header in self.headers:
            self.table.heading(header, text=header)
            self.table.column(header, width=100)


    def add_row(self, integer=None, binary=None, hexa=None):
        # Add a new row to the table
        self.table.insert("", "end", values=(integer, binary, hexa))



if __name__ == "__main__":
    root = tk.Tk()
    app=App(root)
    root.mainloop()