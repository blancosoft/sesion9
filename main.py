import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# ============================
# DATASET
# ============================

X_entrenamiento = np.array([
    [25, 2000, 0],
    [30, 2500, 1],
    [35, 3000, 2],
    [40, 4000, 2],
    [45, 5000, 3],
    [50, 6000, 3],
    [28, 2200, 0],
    [33, 2700, 1],
    [38, 3500, 2],
    [48, 5200, 3]
])

Y_entrenamiento = np.array([0, 0, 1, 1, 1, 1, 0, 0, 1, 1])

# ============================
# FUNCIÓN DE PREDICCIÓN
# ============================

def predecir():
    try:
        edad = int(entry_edad.get())
        salario = int(entry_salario.get())
        hijos = int(entry_hijos.get())
        k = int(entry_k.get())

        if k <= 0:
            raise ValueError

        modelo = KNeighborsClassifier(n_neighbors=k)
        modelo.fit(X_entrenamiento, Y_entrenamiento)

        nuevo = np.array([[edad, salario, hijos]])
        resultado = modelo.predict(nuevo)[0]

        if resultado == 1:
            texto = "✅ El cliente COMPRARÁ"
        else:
            texto = "❌ El cliente NO comprará"

        label_resultado.config(text=texto)

    except:
        messagebox.showerror("Error", "Ingrese valores válidos")

# ============================
# INTERFAZ
# ============================

ventana = tk.Tk()
ventana.title("Clasificador KNN")
ventana.geometry("400x350")
ventana.resizable(False, False)

titulo = tk.Label(ventana, text="Clasificador KNN", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Edad
tk.Label(ventana, text="Edad").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

# Salario
tk.Label(ventana, text="Salario").pack()
entry_salario = tk.Entry(ventana)
entry_salario.pack()

# Hijos
tk.Label(ventana, text="Número de Hijos").pack()
entry_hijos = tk.Entry(ventana)
entry_hijos.pack()

# K
tk.Label(ventana, text="Valor de K").pack()
entry_k = tk.Entry(ventana)
entry_k.pack()

# Botón
btn = tk.Button(ventana, text="Predecir", command=predecir, bg="blue", fg="white")
btn.pack(pady=15)

# Resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 12))
label_resultado.pack()

ventana.mainloop()