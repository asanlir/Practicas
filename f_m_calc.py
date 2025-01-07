from tkinter import *

# Configuración de la ventana principal
root = Tk()
root.title("Calculadora de conversión")
root.geometry('400x200')
root.resizable(False, False)

def convertir():
    """Realiza la conversión seleccionada."""
    try:
        value = float(entrada.get())
        if conversion.get() == "pies_a_metros":
            resultado_valor = round(0.3048 * value, 2)
            resultado_label.config(fg="blue")
            resultado.set(f"{value} pies son {resultado_valor} metros")
        elif conversion.get() == "metros_a_pies":
            resultado_valor = round(value / 0.3048, 2)
            resultado_label.config(fg="blue")
            resultado.set(f"{value} metros son {resultado_valor} pies")
    except ValueError:
        resultado_label.config(fg="red")
        resultado.set("¡Entrada no válida!")

# Configuración del marco principal
frame = Frame(root, pady=10, padx=10)
frame.grid(row=0, column=0, sticky='nsew')

# Configuración de peso de las filas y columnas para que todo se ajuste bien
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Entrada de valor
Label(frame, text="Valor:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
entrada = StringVar()
entrada_input = Entry(frame, width=20, textvariable=entrada)
entrada_input.grid(row=0, column=1, padx=5, pady=5, sticky="w")
entrada_input.focus()

# Selector de conversión
conversion = StringVar(value="pies_a_metros")
Label(frame, text="Conversión:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
Radiobutton(frame,
            text="Pies a metros",
            variable=conversion,
            value="pies_a_metros").grid(row=1, column=1, sticky=W)
Radiobutton(frame,
            text="Metros a pies",
            variable=conversion,
            value="metros_a_pies").grid(row=2, column=1, sticky=W)

# Botón para calcular
Button(frame, text="Convertir", command=convertir).grid(row=3, column=1, columnspan=2, pady=10, sticky="w")

# Salida del resultado
Label(frame, text="Resultado:").grid(row=4, column=0, padx=5, pady=5, sticky=W)
resultado = StringVar()
resultado_label = Label(frame, textvariable=resultado, fg="blue")
resultado_label.grid(row=4, column=1, padx=5, pady=5, sticky=W)

# Atajo para calcular al presionar Enter
root.bind("<Return>", lambda event: convertir())

root.mainloop()
