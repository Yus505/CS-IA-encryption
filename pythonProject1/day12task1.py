from tkinter import *
from tkinter import messagebox


username = "yusif"
password = "yusif"

def mainwindow():
    if username_entry.get() == username and password_entry.get() == password:
        win = Tk()
        win.geometry("500x400")
        win.configure(bg = 'white')


        items = ["apple", "oranges", "banana"]
        prices = [20, 30, 10]

        def addnew():

            win = Tk()
            win.geometry("500x400")
            win.configure(bg = 'white')

            def addition():
                fruit = newfruit_entry.get()
                items.append(fruit)
                items.extend(fruit)
                price = int(price_entry.get())
                prices.append(price)
                items.extend(str(price))
            newfruit_label = Label(win, fg = "black", bg = "white", text = "Add new fruit" , font=("Arial", 25))
            newfruit_label.pack(side = TOP)

            newfruit_entry =  Entry(win,fg = "black", bg = "gray", font=("Arial", 15))
            newfruit_entry.place(x=150, y=90)

            price_label = Label(win, fg = "black", bg = "white", text = "Price" , font=("Arial", 25))
            price_label.place(x=150, y=130)

            price_entry =  Entry(win,fg = "black", bg = "gray", font=("Arial", 15))
            price_entry.place(x=150, y=180)

            calculate_button =  Button(win,fg = "white",text = "add", bg = "gray", font=("Arial",15),command=addition)
            calculate_button.place(x=210, y=270)

            win.mainloop()


        def calculatetotal():

            win = Tk()
            win.geometry("500x400")
            win.configure(bg = 'white')

            def calculate():
                number = int(position_entry.get())
                amount = int(quantity_entry.get())
                print(f"You chose {items[number]} and it costs {prices[number] * amount} $")

            position_label = Label(win, fg = "black", bg = "white", text = "Poisition (index) of item" , font=("Arial", 25))
            position_label.pack(side = TOP)

            position_entry =  Entry(win,fg = "black", bg = "gray", font=("Arial", 15))
            position_entry.place(x=150, y=90)

            quantity_label = Label(win, fg = "black", bg = "white", text = "Quantity(kg)" , font=("Arial", 25))
            quantity_label.place(x=150, y=130)

            quantity_entry =  Entry(win,fg = "black", bg = "gray", font=("Arial", 15))
            quantity_entry.place(x=150, y=180)

            calculate_button =  Button(win,fg = "white",text = "Calculate", bg = "gray", font=("Arial",15),command=calculate)
            calculate_button.place(x=210, y=270)

            win.mainloop()


        newfruit_button =  Button(win,fg = "white",text = "Add New Fruits", bg = "gray", font=("Arial",15),command=addnew)
        newfruit_button.pack(side = TOP)

        calculatetotal_button =  Button(win,fg = "white",text = "Calculate Totals", bg = "gray", font=("Arial",15),command=calculatetotal)
        calculatetotal_button.pack(side = BOTTOM)
    else:
        message = ("You inserted wrong username or password")
    messagebox.showinfo("You credentials", message)


win = Tk()
win.geometry("500x400")
win.configure(bg = 'white')

username_label = Label(win, fg="black", bg="white", text="username:", font=("Arial", 25))
username_label.pack(side=TOP)

username_entry = Entry(win, fg="black", bg="gray", font=("Arial", 15))
username_entry.place(x=150, y=90)

password_label = Label(win, fg="black", bg="white", text="password:", font=("Arial", 25))
password_label.place(x=150, y=130)

password_entry = Entry(win, fg="black", bg="gray", show = "*", font=("Arial", 15))
password_entry.place(x=150, y=180)

calculate_button = Button(win, fg="white", text="Login", bg="gray", font=("Arial", 15), command=mainwindow)
calculate_button.place(x=210, y=270)



win.mainloop()
