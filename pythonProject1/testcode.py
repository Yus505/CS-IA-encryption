import tkinter as tk
from PIL import Image, ImageTk

# Create a new tkinter window
window = tk.Tk()

# Create a label to display the menu title
title_label = tk.Label(window, text="Food Menu", font=("Arial", 18))
title_label.pack()

# Load the image for food 1
food1_image = Image.open("burger.jpg")
food1_image = food1_image.resize((100, 100))
tk_food1_image = ImageTk.PhotoImage(food1_image)

# Create a label for food 1, displaying the image and its name and price
food1_label = tk.Label(window, text="Cheeseburger $5", image=tk_food1_image, compound="top")
food1_label.image = tk_food1_image
food1_label.pack()

# Load the image for food 2
food2_image = Image.open("salad.png")
food2_image = food2_image.resize((100, 100))
tk_food2_image = ImageTk.PhotoImage(food2_image)

# Create a label for food 2, displaying the image and its name and price
food2_label = tk.Label(window, text="Pizza $8", image=tk_food2_image, compound="top")
food2_label.image = tk_food2_image
food2_label.pack()

# Start the tkinter event loop
window.mainloop()
