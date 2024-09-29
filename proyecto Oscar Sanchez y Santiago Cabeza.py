import tkinter as tk
from tkinter import messagebox
import math


def maclaurin_sen(x, terms=15):  
    sen_x = 0
    for n in range(terms):
        sign = (-1) ** n
        sen_x += sign * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return sen_x


def maclaurin_cos(x, terms=15):
    cos_x = 0
    for n in range(terms):
        sign = (-1) ** n
        cos_x += sign * (x ** (2 * n)) / math.factorial(2 * n)
    return cos_x


def cot(x):
    try:
        return 1 / math.tan(x)
    except ZeroDivisionError:
        raise ValueError("Cot no está definida para este valor.")


def sec(x):
    try:
        return 1 / maclaurin_cos(x) if abs(x) < 2 else 1 / math.cos(x)  
    except ZeroDivisionError:
        raise ValueError("Sec no está definida para este valor.")


def csc(x):
    try:
        return 1 / maclaurin_sen(x) if abs(x) < 2 else 1 / math.sin(x)  
    except ZeroDivisionError:
        raise ValueError("Csc no está definida para este valor.")


def calcular_formula():
    try:
        formula = formula_entry.get()

   
        formula = formula.replace("sen", "maclaurin_sen")  
        formula = formula.replace("cos", "maclaurin_cos")  
        formula = formula.replace("tan", "math.tan")       
        formula = formula.replace("cot", "cot")            
        formula = formula.replace("sec", "sec")            
        formula = formula.replace("csc", "csc")            
        formula = formula.replace("^", "**")               

       
        resultado.set(f"{eval(formula):.8f}")

    except (ValueError, SyntaxError, ZeroDivisionError) as e:
        messagebox.showerror("Error", f"Error en la expresión: {e}")


def clear_fields():
    formula_entry.delete(0, tk.END)
    resultado.set("")


root = tk.Tk()
root.title("Calculadora con Series de Maclaurin")

resultado = tk.StringVar()

tk.Label(root, text="Introduce tu fórmula:").grid(row=0, column=0)
formula_entry = tk.Entry(root, width=30)
formula_entry.grid(row=0, column=1)

tk.Button(root, text="Calcular", command=calcular_formula).grid(row=1, column=1)
tk.Button(root, text="Limpiar", command=clear_fields).grid(row=1, column=2)

tk.Label(root, text="Resultado:").grid(row=2, column=0)
tk.Label(root, textvariable=resultado).grid(row=2, column=1)

root.mainloop()









