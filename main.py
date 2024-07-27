import tkinter as tk

def perform_conversion():
    conversion_type = conversion_type_var.get()
    value = float(input_entry.get())

    if conversion_type == "Miles to Kms":
        result = value * 1.609
    elif conversion_type == "Kms to Miles":
        result = value / 1.609
    elif conversion_type == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
    elif conversion_type == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9
    elif conversion_type == "Inches to Centimeters":
        result = value * 2.54
    elif conversion_type == "Centimeters to Inches":
        result = value / 2.54
    elif conversion_type == "Pounds to Kilograms":
        result = value * 0.45359237
    elif conversion_type == "Kilograms to Pounds":
        result = value / 0.45359237

    result_label["text"] = str(result)

root = tk.Tk()
root.title("Conversion Calculator")
root.minsize(width=200, height=100)
root.config(padx=30, pady=30)

conversion_type_var = tk.StringVar(root)
conversion_type_var.set("Miles to Kms")  # Default conversion type

conversion_type_label = tk.Label(root, text="Conversion Type")
conversion_type_label.grid(column=0, row=0)

conversion_type_dropdown = tk.OptionMenu(root, conversion_type_var, "Miles to Kms", "Kms to Miles", "Celsius to Fahrenheit", "Fahrenheit to Celsius", "Inches to Centimeters", "Centimeters to Inches", "Pounds to Kilograms", "Kilograms to Pounds")
conversion_type_dropdown.grid(column=1, row=0)

input_label = tk.Label(root, text="Value")
input_label.grid(column=0, row=1)

input_entry = tk.Entry(root)
input_entry.grid(column=1, row=1)

calculate_button = tk.Button(root, text="Calculate", command=perform_conversion)
calculate_button.grid(column=1, row=2)

result_label = tk.Label(root, text="Result")
result_label.grid(column=0, row=3, columnspan=2)

root.mainloop()
