from tkinter import *
from tkinter import messagebox

new_window = Tk()
new_window.geometry("500x400")
new_window.configure(bg = 'pink')
border_color = Frame(new_window, background = "black")
def calculate():
    message = (f"{name_entry.get()} you have lived {str(int(age_entry.get())*365)} days")
    messagebox.showinfo("The amount of days you have lived", message)

name_label =  Label(new_window, fg = "black", bg = "pink", text = "Name", font=("Arial", 40))
name_label.pack(side = TOP)

name_entry =  Entry(new_window,fg = "black", bg = "white", font=("Arial", 30))
name_entry.pack(side = TOP)


age_label =  Label(new_window,fg = "black", bg = "pink",text = "Age", font=("Arial", 40))
age_label.pack(side = TOP)

age_entry =  Entry(new_window,fg = "black", bg = "white", font=("Arial", 30))
age_entry.pack(side = TOP)

calculate_button =  Button(new_window,fg = "black",text = "Click", bg = "white", font=("Arial",28), command=calculate)
calculate_button.place(x=190, y=270)

new_window.mainloop()