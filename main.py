from tkinter import *

#create new window
window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

#create entry box

entry = Entry(width=7)
entry.insert(END, string="0")
entry.grid(column=1,row=0)
miles = entry.get()

#create label "miles"

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#create label "is equal to"

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

#create km conversion answer label

answer = Label(text="0")
answer.grid(column=1, row=1)

#create label "Km"

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#create calculate button

def calculate():
    global answer
    user_entry = float(entry.get())
    km = user_entry * 1.60934
    answer.config(text=f"{round(km,2)}")

calculate = Button(text="Calculate", command=calculate)
calculate.grid(column=1, row=2)

window.mainloop()