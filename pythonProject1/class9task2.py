from tkinter import *
from tkinter import messagebox
import random

number1 = random.randint(1,10)
number2 = random.randint(1,10)

new_window = Tk()
new_window.geometry("500x400")
new_window.configure(bg = 'cyan')
actual_answer = int(number1 * number2)

def calculate():
    if int(your_answer_entry.get()) == actual_answer:
        message = ("You are right")
    else:
        message = (f"You are wrong, the answer is {actual_answer}")
    messagebox.showinfo("Your answer", message)


calculation_label =  Label(new_window, fg = "black", bg = "lightgreen", text = (f"What is {number1} x {number2}?") , font=("Arial", 33))
calculation_label.place(x=110, y=50)

your_answer_entry =  Entry(new_window,fg = "black", bg = "white", font=("Arial", 20))
your_answer_entry.place(x=100, y=150)

calculate_button =  Button(new_window,fg = "white",text = "Check", bg = "blue", font=("Arial",28),command=calculate)
calculate_button.place(x=190, y=270)

reset_button =  Button(new_window,fg = "white",text = "Check", bg = "blue", font=("Arial",28),command=calculate)
reset_button.pack(side= TOP)

new_window.mainloop()