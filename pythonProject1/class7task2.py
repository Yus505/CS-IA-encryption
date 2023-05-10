import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, bg="pink")
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)
canvas1.create_text(200, 100, text="Hello There", fill="black", font=('Helvetica 15 bold'))


def get_square_root():
    x1 = entry1.get()

    label1 = tk.Label(root, text=float(x1) ** 0.5)
    canvas1.create_window(200, 230, window=label1)


button1 = tk.Button(text='click')
canvas1.create_window(200, 180, window=button1)

root.mainloop()