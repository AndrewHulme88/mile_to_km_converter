import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometers")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()

def button_clicked():
    my_label["text"] = input.get()

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

input = tkinter.Entry()
input.pack()

window.mainloop()
