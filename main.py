from tkinter import *

def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.grid(padx=5, pady=5)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.grid(padx=5, pady=5)

label_3 = Label(text="KM")
label_3.grid(column=2, row=1)
label_3.grid(padx=5, pady=5)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)
km_result_label.config(padx=5, pady=5)

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)
calc_button.config(padx=5, pady=5)

miles_input = Entry(width=10)
miles_input.insert(0, "0")
miles_input.grid(column=1, row=0)


window.mainloop()

