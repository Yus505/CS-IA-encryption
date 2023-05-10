import tkinter as tk
from tkinter import ttk, messagebox
from fpdf import FPDF


class App:
    def __init__(self, root):
        root.title("Table with Converter")
        self.table = Table(root)
        self.integer_entry = tk.Entry(root)
        self.binary_entry = tk.Entry(root)
        self.hexadecimal_entry = tk.Entry(root)
        self.integer_entry.bind("<Return>", lambda _: self.add_row())
        self.binary_entry.bind("<Return>", lambda _: self.add_row())
        self.hexadecimal_entry.bind("<Return>", lambda _: self.add_row())
        self.integer_entry.grid(row=1, column=0)
        self.binary_entry.grid(row=1, column=1)
        self.hexadecimal_entry.grid(row=1, column=2)
        self.quiz_button = tk.Button(root, text="Quiz", command=self.quiz)
        self.download_pdf_button = tk.Button(root, text="Download PDF", command=self.download_pdf)
        self.quiz_button.grid(row=2, column=0)
        self.download_pdf_button.grid(row=2, column=2)

    def add_row(self):
        try:
            integer = int(self.integer_entry.get())
            binary = int(self.binary_entry.get(), 2)
            hexadecimal = int(self.hexadecimal_entry.get(), 16)
        except ValueError:
            messagebox.showerror("Error", "Invalid input")
            return
        self.table.add_row(integer=integer, binary=binary, hexadecimal=hexadecimal)
        self.integer_entry.delete(0, tk.END)
        self.binary_entry.delete(0, tk.END)
        self.hexadecimal_entry.delete(0, tk.END)

    def quiz(self):
        pass

    def download_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for i, header in enumerate(self.table.headers):
            pdf.cell(40, 10, header.title(), border=1)
        pdf.ln()
        for row in self.table.table.get_children():
            values = self.table.table.item(row)["values"]
            for value in values:
                pdf.cell(40, 10, str(value), border=1)
            pdf.ln()
        pdf.output("table.pdf")


class Table:
    def __init__(self, root):
        self.headers = ["Integer", "Binary", "Hexadecimal"]
        self.table = ttk.Treeview(root, columns=self.headers, show="headings")
        for header in self.headers:
            self.table.heading(header, text=header)
        self.table.grid(row=0, column=0, columnspan=3)

    def add_row(self, integer, binary, hexadecimal):
        self.table.insert("", "end", values=[integer, bin(binary)[2:], hex(hexadecimal)[2:]])


root = tk.Tk()
app = App(root)
root.mainloop()
