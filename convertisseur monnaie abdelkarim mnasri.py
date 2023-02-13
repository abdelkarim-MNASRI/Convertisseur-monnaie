import tkinter as tk
from forex_python.converter import CurrencyRates

c = CurrencyRates()

def convert():
    try:
        amount = float(entry_amount.get())
        from_currency = entry_from.get()
        to_currency = entry_to.get()
        result = c.convert(from_currency, to_currency, amount)
        label_result.config(text=result)
        # sauvegarder l'historique des conversions
        with open("conversion_history.txt", "a") as f:
            f.write(f"{amount} {from_currency} = {result} {to_currency}\n")
    except:
        label_result.config(text="Conversion impossible")

root = tk.Tk()
root.title("Convertisseur de devises")

label_amount = tk.Label(root, text="Montant à convertir :")
entry_amount = tk.Entry(root)

label_from = tk.Label(root, text="Devise de départ :")
entry_from = tk.Entry(root)

label_to = tk.Label(root, text="Devise cible :")
entry_to = tk.Entry(root)

label_result = tk.Label(root, text="")

convert_button = tk.Button(root, text="Convertir", command=convert)

label_amount.grid(row=0, column=0)
entry_amount.grid(row=0, column=1)
label_from.grid(row=1, column=0)
entry_from.grid(row=1, column=1)
label_to.grid(row=2, column=0)
entry_to.grid(row=2, column=1)
convert_button.grid(row=3, column=0)
label_result.grid(row=4, column=0)

root.mainloop()
