import tkinter as tk
from tkinter import messagebox
from forex_python.converter import CurrencyRates

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combobox_from.get()
    to_currency = combobox_to.get()

    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)

    messagebox.showinfo("Result", f"{amount} {from_currency} = {result} {to_currency}")

# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Create the input fields and labels
label_amount = tk.Label(window, text="Amount:")
label_amount.pack()

entry_amount = tk.Entry(window)
entry_amount.pack()

label_from = tk.Label(window, text="From:")
label_from.pack()

combobox_from = tk.ttk.Combobox(window, values=["USD", "EUR", "GBP", "INR"])
combobox_from.pack()

label_to = tk.Label(window, text="To:")
label_to.pack()

combobox_to = tk.ttk.Combobox(window, values=["USD", "EUR", "GBP", "INR"])
combobox_to.pack()

# Create the convert button
button_convert = tk.Button(window, text="Convert", command=convert_currency)
button_convert.pack()

# Start the main event loop
window.mainloop()
