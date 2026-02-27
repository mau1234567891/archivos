import tkinter as tk
from tkinter import messagebox

def obtener_valores():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        return num1, num2
    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos")
        return None, None

def sumar():
    num1, num2 = obtener_valores()
    if num1 is not None:
        resultado.set(num1 + num2)

def restar():
    num1, num2 = obtener_valores()
    if num1 is not None:
        resultado.set(num1 - num2)

def multiplicar():
    num1, num2 = obtener_valores()
    if num1 is not None:
        resultado.set(num1 * num2)

def dividir():
    num1, num2 = obtener_valores()
    if num1 is not None:
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre 0")
        else:
            resultado.set(num1 / num2)

# Ventana principal
ventana = tk.Tk()
ventana.title("ASPDEV - App de Aritmética")
ventana.geometry("350x300")
ventana.resizable(False, False)

# Título
tk.Label(ventana, text="Formulario Aritmético",
         font=("Arial", 14, "bold")).pack(pady=10)

# Entrada 1
tk.Label(ventana, text="Número 1").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

# Entrada 2
tk.Label(ventana, text="Número 2").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

tk.Button(frame_botones, text="➕ Sumar", width=10, command=sumar).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="➖ Restar", width=10, command=restar).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botones, text="✖ Multiplicar", width=10, command=multiplicar).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="➗ Dividir", width=10, command=dividir).grid(row=1, column=1, padx=5, pady=5)

# Resultado
tk.Label(ventana, text="Resultado").pack(pady=5)
resultado = tk.StringVar()
tk.Entry(ventana, textvariable=resultado, state="readonly").pack()

# Ejecutar
ventana.mainloop()