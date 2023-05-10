import random
import tkinter as tk

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

class Table(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        headers = ['Hexadecimal', 'Binary', 'Integer']
        for j, header in enumerate(headers):
            label = tk.Label(self, text=header, font=('Arial', 16, 'bold'), fg='white', bg='gray')
            label.grid(row=0, column=j)

        self.cells = []
        for i in range(rows):
            row_cells = []
            for j in range(columns):
                cell = tk.Entry(self, text='', font=('Arial', 16))
                cell.grid(row=i+1, column=j)
                row_cells.append(cell)
            self.cells.append(row_cells)

        # Add the Download PDF button
        download_button = tk.Button(self, text='Download PDF', font=('Arial', 16), command=self.download_pdf)
        download_button.grid(row=rows+1, column=0, columnspan=columns, pady=10)

    def set_cell(self, row, column, value):
        self.cells[row][column].delete(0, tk.END)
        self.cells[row][column].insert(0, value)

    def get_cell(self, row, column):
        return self.cells[row][column].get().replace('0x', '').replace('0b', '')

    def download_pdf(self):
        # Create a new PDF file
        c = canvas.Canvas('table.pdf', pagesize=letter)

        # Define the column widths
        col_widths = [2 * inch, 2 * inch, 1 * inch]

        # Define the row heights
        row_heights = []
        for i in range(len(self.cells)):
            row_heights.append(0.5 * inch)

        # Draw the table headers
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.setFont('Helvetica-Bold', 14)
        for i, header in enumerate(['Hexadecimal', 'Binary', 'Integer']):
            c.drawCentredString(sum(col_widths[:i + 1]) - col_widths[i] / 2.0, 10.5 * inch, header)

        # Draw the table cells
        c.setFillColorRGB(0, 0, 0)
        c.setFont('Helvetica', 12)
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                c.drawString(sum(col_widths[:j]), 10 * inch - sum(row_heights[:i + 1]), cell.get())

        # Draw the horizontal and vertical lines
        c.setStrokeColorRGB(0, 0, 0)
        c.setLineWidth(1)
        c.line(0.5 * inch, 10 * inch, 7.5 * inch, 10 * inch)
        c.line(0.5 * inch, 10 * inch, 0.5 * inch, 0.5 * inch)
        c.line(2.5 * inch, 10 * inch, 2.5 * inch, 0.5 * inch)
        c.line(4.5 * inch, 10 * inch, 4.5 * inch, 0.5 * inch)
        c.line(6.5 * inch, 10 * inch, 6.5 * inch, 0.5 * inch)
        c.line(0.5 * inch, 0.5 * inch, 0.5 * inch, 0.5 * inch)

        # Save the PDF file
        c.showPage()
        c.save()


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



quiz_button = tk.Button(root, text='Quiz', font=('Arial', 16), command=quiz)
quiz_button.pack(pady=10)

root.mainloop()

