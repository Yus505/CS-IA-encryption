from tkinter import *
from tkinter import ttk
import json

gender = ["male", "female", "non-binary"]


def save_info():
    name_info = NameOfStudent_entry.get()
    gender_info = gender_entry.get()
    mark = Mark_entry.get()

    data = {}
    data['Name'] = name_info
    data['Gender'] = gender_info
    data['Mark'] = mark

    with open("myfile.json", "r") as file:
        data = json.load(file)
    data.append(students)

    out_file = open("myfile.json", "w")
    json.dump(data, out_file)
    students.insert("",'end', iid=None,
                values=(NameOfStudent_entry.get(), gender_entry.get(), Mark_entry.get()))


def generate():
    def StudentMark():
        if int(Mark_entry.get()) > 90:
            mark = 7
        elif int(Mark_entry.get()) > 75:
            mark = 6
        elif int(Mark_entry.get()) > 60:
            mark = 5
        elif int(Mark_entry.get()) > 50:
            mark = 4
        elif int(Mark_entry.get()) > 40:
            mark = 3
        elif int(Mark_entry.get()) > 30:
            mark = 2
        else:
            mark = 1


        if gender_entry.get() == 'female':
            gender = "she"
        elif gender_entry.get() == 'male':
            gender = "he"
        else:
            gender = "they"
        if mark < 7:
            print(f"{NameOfStudent_entry.get()} got {Mark_entry.get()}%, which is {mark} from the ib points. In order to get higher mark {gender} needs to study harder")
        else:
            print(f"{NameOfStudent_entry.get()} got {Mark_entry.get()}%, which is {mark} from the ib points. {gender} got the highest mark")

win = Tk()
win.geometry("600x400")
win.configure(bg = 'white')
win.title("Student Database")
tabholder = ttk.Notebook(win)

tab1 = ttk.Frame(tabholder)
tabholder.add(tab1, text = 'Add new student')

tab2 = ttk.Frame(tabholder)
tabholder.add(tab2, text = 'Display')

tabholder.pack(expand=1,fill="both")

username_label = Label(tab1, fg="black", bg="white", text="Comment Generator", font=("Arial", 25))
username_label.pack(side=TOP)


NameOfStudent_label = Label(tab1, fg="black", bg="white", text="Name of student", font=("Arial", 15))
NameOfStudent_label.place(x=150, y=60)

NameOfStudent_entry = Entry(tab1, fg="black", bg="white", font=("Arial", 15))
NameOfStudent_entry.place(x=150, y=90)

gender_label = Label(tab1, fg="black", bg="white", text="Gender", font=("Arial", 15))
gender_label.place(x=20, y=140)

gender_entry = ttk.Combobox(tab1, values = gender, font=("Arial", 15))
gender_entry.set("Pick your gender")
gender_entry.place(x=20, y=180)

Mark_label = Label(tab1, fg="black", bg="white", text="Mark", font=("Arial", 15))
Mark_label.place(x=300, y=140)

Mark_entry = Entry(tab1, fg="black", bg="white", font=("Arial", 15))
Mark_entry.place(x=300, y=180)

calculate_button = Button(tab1, fg="white", text="Generate & Save", bg="gray", font=("Arial", 15), command=save_info)
calculate_button.place(x=210, y=270)

students = ttk.Treeview(tab2, columns=('#1','#2', '#3'), height=25)
students.heading('#1', text='Name')
students.heading('#2', text='Gender')
students.heading('#3', text='Mark')


students.column('#0',stretch=NO, width=0)

students.grid()
treeview = True




students.pack()


win.mainloop()


