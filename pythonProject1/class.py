import random
import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF

class Table(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        headers = ['Hexadecimal', 'Binary', 'Integer']
        for j, header in enumerate(headers):
            label = tk.Label(self, text=header, font=('Arial', 16, 'bold'), fg='white', bg='gray')
            label.grid(row=0, column=j)

        self.cells = []
        for i in range(rows):
            if i > 20:  # Only display rows up to 255
                break
            row_cells = []
            for j in range(columns):
                cell = tk.Entry(self, text='', font=('Arial', 16))
                cell.grid(row=i+1, column=j)
                row_cells.append(cell)
            self.cells.append(row_cells)

    def set_cell(self, row, column, value):
        self.cells[row][column].delete(0, tk.END)
        self.cells[row][column].insert(0, value)

    def get_cell(self, row, column):
        return self.cells[row][column].get().replace('0x', '').replace('0b', '')

    def save_as_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(60, 10, 'Hexadecimal', 1)
        pdf.cell(60, 10, 'Binary', 1)
        pdf.cell(60, 10, 'Integer', 1)
        pdf.ln()
        pdf.set_font('Arial', '', 16)
        for row in self.cells:
            pdf.cell(60, 10, row[0].get(), 1)
            pdf.cell(60, 10, row[1].get(), 1)
            pdf.cell(60, 10, row[2].get(), 1)
            pdf.ln()
        file = filedialog.asksaveasfilename(defaultextension='.pdf')
        if file:
            pdf.output(file)
        save_button = tk.Button(self, text='Save as PDF', command=self.save_as_pdf)
        save_button.pack(pady=10)

root = tk.Tk()
root.title('Table')

table = Table(root, rows=20, columns=3)
table.pack(padx=10, pady=10)

for i in range(20):
    table.set_cell(i, 0, hex(i).replace('0x', ''))
    table.set_cell(i, 1, bin(i).replace('0b', ''))
    table.set_cell(i, 2, str(i))

def quiz():
    # Initialize score and question counter
    score = 0
    question_count = 0

    # Define a function to check the answer
    def check_answer():
        nonlocal value, row, col, question, score, question_count

        # Increment question counter
        question_count += 1

        # Get user's answer and expected answer
        answer = answer_entry.get()
        expected_answer = value

        # Check the answer and update the score
        if answer == expected_answer:
            result = 'Correct!'
            score += 1
        else:
            result = f'Incorrect. The answer is {expected_answer}'

        # Update the result label
        result_label.configure(text=result)

        # If the user has answered 10 questions, show the final score and disable the quiz button
        if question_count == 10:
            quiz_button.config(state=tk.DISABLED)
            final_score = f'Final score: {score}/10'
            final_score_label.configure(text=final_score)
        else:
            # Otherwise, generate a new question
            row = random.randint(0, 20)
            col = random.randint(0, 2)
            value = table.get_cell(row, col)
            question = f"What is the {['hexadecimal', 'binary', 'integer'][col]} representation of {row}?"
            question_label.configure(text=question)
            answer_entry.delete(0, 'end')

    # Generate the first question
    row = random.randint(0, 20)
    col = random.randint(0, 2)
    value = table.get_cell(row, col)
    question = f"What is the {['hexadecimal', 'binary', 'integer'][col]} representation of {row}?"

    # Create the quiz popup window
    popup = tk.Toplevel(root)
    popup.title('Quiz')
    popup.geometry('400x200')

    # Create the widgets in the popup window
    question_label = tk.Label(popup, text=question, font=('Arial', 16))
    question_label.pack(pady=10)

    answer_entry = tk.Entry(popup, font=('Arial', 16))
    answer_entry.pack(pady=10)

    check_button = tk.Button(popup, text='Check Answer', command=check_answer)
    check_button.pack(pady=10)

    result_label = tk.Label(popup, font=('Arial', 16))
    result_label.pack()

    final_score_label = tk.Label(popup, font=('Arial', 16))
    final_score_label.pack()


# Add a button to save the table as a PDF


def save_as_pdf(self):
    """
    Save the table as a PDF file.
    """
    # Set up the PDF document
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    # Add the headers
    headers = ['Hexadecimal', 'Binary', 'Integer']
    for j, header in enumerate(headers):
        pdf.cell(50, 10, header, 1)
    pdf.ln()

    # Add the data
    for i in range(len(self.cells)):
        if i > 20:
            break
        for j in range(len(self.cells[i])):
            value = self.get_cell(i, j)
            pdf.cell(50, 10, value, 1)
        pdf.ln()

    # Save the PDF file
    pdf.output('table.pdf', 'F')




root.mainloop()
quiz_button = tk.Button(root, text='Quiz', font=('Arial', 16), command=quiz)
quiz_button.pack(pady=10)

root.mainloop()