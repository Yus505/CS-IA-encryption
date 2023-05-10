from tkinter import *
from tkinter import messagebox

new_window = Tk()
new_window.geometry("500x400")
new_window.configure(bg = 'pink')
border_color = Frame(new_window, background = "black")
def calculate():
    message = (f"Your BMI is {round(float(weight_entry.get())/ (float(height_entry.get()) **2))} ")
    messagebox.showinfo("Your BMI", message)

height_label =  Label(new_window, fg = "black", bg = "pink", text = "Height", font=("Arial", 40))
height_label.pack(side = TOP)

height_entry =  Entry(new_window,fg = "black", bg = "white", font=("Arial", 30))
height_entry.pack(side = TOP)


weight_label =  Label(new_window,fg = "black", bg = "pink",text = "Weight", font=("Arial", 40))
weight_label.pack(side = TOP)

weight_entry =  Entry(new_window,fg = "black", bg = "white", font=("Arial", 30))
weight_entry.pack(side = TOP)

calculate_button =  Button(new_window,fg = "black",text = "Click", bg = "white", font=("Arial",28), command=calculate)
calculate_button.place(x=190, y=270)

new_window.mainloop()