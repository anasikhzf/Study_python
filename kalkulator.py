import tkinter as tk
from tkinter import messagebox

def hitung():
    try:
        ekspresi = inputan.get()
        hasil = eval(ekspresi)
        inputan.delete(0, tk.END)
        inputan.insert(tk.END, str(hasil))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def hapus():
    inputan.delete(0, tk.END)

root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("300x400")
root.configure(bg='#F5F5F5')

inputan = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 14))
inputan.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

tombol = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (teks, baris, kolom) in tombol:
    tombol = tk.Button(root, text=teks, padx=20, pady=10, font=("Arial", 12), bg='#CCCCCC', activebackground='#999999',
                       command=lambda t=teks: inputan.insert(tk.END, t))
    tombol.grid(row=baris, column=kolom, padx=5, pady=5)

tombol_hapus = tk.Button(root, text="Hapus", padx=50, pady=10, font=("Arial", 12), bg='#FF5733', activebackground='#FF8C65',
                         command=hapus)
tombol_hapus.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

tombol_hitung = tk.Button(root, text="Hitung", padx=50, pady=10, font=("Arial", 12), bg='#4CAF50', activebackground='#81C784',
                          command=hitung)
tombol_hitung.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
