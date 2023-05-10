from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

win = Tk()
win.geometry("500x400")
win.configure(bg = 'lightpink')

def calculate():
    expected_life = (int(expected_entry.get()) - int(current_entry.get()))
    current_value = (int(initial_entry.get()) / int(expected_entry.get()) * int(expected_life))
    # value_of_car = print(f"Your car has {expected_life} years left to its end of life, its current value is ${int(current_value)}")
    text_label =  Label(win, fg = "black", bg = "lightpink", text = f"Your car has {expected_life} years left to its end \nof life, its current value is ${int(current_value)}", font=("Arial", 15))
    text_label.place(x = 100, y = 330)

calculation_label = Label(win, fg = "black", bg = "lightpink", text = "Depreciation Calculator" , font=("Arial", 25))
calculation_label.pack(side = TOP)

initial_label =  Label(win, fg = "black", bg = "lightpink", text = "Initial Value" , font=("Arial", 20))
initial_label.place(x = 190, y = 50)

initial_entry =  Entry(win,fg = "black", bg = "white", font=("Arial", 15))
initial_entry.place(x=150, y=90)

expected_label =  Label(win, fg = "black", bg = "lightpink", text = "Expected Life" , font=("Arial", 20))
expected_label.place(x = 190, y = 130)

expected_entry =  Entry(win,fg = "black", bg = "white", font=("Arial", 15))
expected_entry.place(x=150, y=170)

current_label =  Label(win, fg = "black", bg = "lightpink", text = "Current Age" , font=("Arial", 20))
current_label.place(x = 190, y = 200)

current_entry =  Entry(win,fg = "black", bg = "white", font=("Arial", 15))
current_entry.place(x=150, y=240)

calculate_button =  Button(win,fg = "white",text = "Calculate", bg = "lightgreen", font=("Arial",15),command=calculate)
calculate_button.place(x=210, y=270)

pb = ttk.Progressbar(
    win,
    orient='horizontal',
    mode='determinate',
    length=280
)
pb.place(x=120, y = 320)
win.mainloop()