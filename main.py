import tkinter

def miles_to_kms():
    miles = float(input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Kms")
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=miles_to_kms)
button.grid(column=1, row=2)

input = tkinter.Entry()
input.grid(column=1, row=0)

equals_label = tkinter.Label(text="Equals:")
equals_label.grid(column=0, row=1)

result_label = tkinter.Label(text="0")
result_label.grid(column=1, row=1)

window.mainloop()
