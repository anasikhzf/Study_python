import tkinter as tk
from tkinter import messagebox

def hitung_suhu():
    try:
        suhu = float(input_entry.get())
        satuan = satuan_var.get()

        if satuan == "Celcius":
            reamur = suhu * 4/5
            fahrenheit = (suhu * 9/5) + 32
            kelvin = suhu + 273
            hasil_text.set(f"Reamur: {reamur:.2f} derajat\nFahrenheit: {fahrenheit:.2f} derajat\nKelvin: {kelvin:.2f} derajat")
        elif satuan == "Reamur":
            celcius = suhu * 5/4
            fahrenheit = (suhu * 9/4) + 32
            kelvin = (suhu * 5/4) + 273
            hasil_text.set(f"Celcius: {celcius:.2f} derajat\nFahrenheit: {fahrenheit:.2f} derajat\nKelvin: {kelvin:.2f} derajat")
        elif satuan == "Fahrenheit":
            celcius = (5/9) * (suhu - 32)
            reamur = (4/9) * (suhu - 32)
            kelvin = (5/9) * (suhu - 32) + 273
            hasil_text.set(f"Celcius: {celcius:.2f} derajat\nReamur: {reamur:.2f} derajat\nKelvin: {kelvin:.2f} derajat")
        elif satuan == "Kelvin":
            celcius = suhu - 273
            reamur = (4/5) * (suhu - 273)
            fahrenheit = (9/5) * (suhu - 273) + 32
            hasil_text.set(f"Celcius: {celcius:.2f} derajat\nReamur: {reamur:.2f} derajat\nFahrenheit: {fahrenheit:.2f} derajat")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Membuat GUI
root = tk.Tk()
root.title("Konversi Suhu")
root.geometry("400x300")
root.configure(bg='#F5F5F5')

# Label
label_suhu = tk.Label(root, text="Masukkan suhu:", font=("Arial", 12), bg='#F5F5F5')
label_suhu.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Entry
input_entry = tk.Entry(root, width=20, font=("Arial", 12))
input_entry.grid(row=0, column=1, padx=10, pady=10)

# Dropdown untuk pilihan satuan suhu
satuan_var = tk.StringVar(root)
satuan_var.set("Celcius")  # Default value

satuan_label = tk.Label(root, text="Pilih satuan suhu:", font=("Arial", 12), bg='#F5F5F5')
satuan_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

satuan_option = tk.OptionMenu(root, satuan_var, "Celcius", "Reamur", "Fahrenheit", "Kelvin")
satuan_option.config(font=("Arial", 12))
satuan_option.grid(row=1, column=1, padx=10, pady=10)

# Tombol Hitung
tombol_hitung = tk.Button(root, text="Hitung", font=("Arial", 12), bg='#4CAF50', activebackground='#81C784',
                          command=hitung_suhu)
tombol_hitung.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Hasil
hasil_text = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil_text, font=("Arial", 12), bg='#F5F5F5')
hasil_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
