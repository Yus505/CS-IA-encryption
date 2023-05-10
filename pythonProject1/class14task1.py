# Import required libraries
from tkinter import *


win = Tk()
win.geometry("700x500")



frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)



def addition():
    global integer
    integer += 1
    print(integer)

img = PhotoImage(file="img//png-transparent-mcdonald-s-cheeseburger-hamburger-mcdonald-s-big-mac-fast-food-menu-thumbnail.png")
bg_lbl = Label(image=img)
bg_lbl.place(x=10, y=60)

integer = 0


img1 = PhotoImage(file="img//kfc_food.png")
bg_lbl = Label(image=img1)
bg_lbl.place(x=310,y=60)


food_menu_label = Label(win, fg="black", bg="white", text="Food Menu Thing", font=("Arial", 25))
food_menu_label.pack(side=TOP)

mcdonalds_label = Label(win, fg="black", bg="white", text="McDonald's burger", font=("Arial", 15))
mcdonalds_label.place(x=50, y=50)

kfc_label = Label(win, fg="black", bg="white", text="KFC family bucket", font=("Arial", 15))
kfc_label.place(x=500, y=50)

addition_button = Button(win, fg="white", text="Generate & Save", bg="gray", font=("Arial", 15), command=addition)
addition_button.place(x=210, y=270)

calculate_button = Button(win, fg="white", text="Generate & Save", bg="gray", font=("Arial", 15), command=addition)
calculate_button.place(x=210, y=270)

win.mainloop()