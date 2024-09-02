"""
Este pequeño script toma un archivo .csv con elementos ordenados aleatoriamente y devuelve
un archivo .txt con los elementos ordenados
"""

import csv
from collections import Counter

# Especificar la ruta del archivo CSV
archivo = "<ruta del archivo>.csv"

# Abrir y leer el archivo CSV
with open(archivo, mode='r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Filtrar las filas que tienen un valor en la columna de posiciones
# (asumimos que es la segunda columna, índice 1)
filtered_rows = [row for row in rows if row[1].strip()]

# Obtener los valores de la columna de posiciones para verificar duplicados
positions = [row[1].strip() for row in filtered_rows]

# Contar las ocurrencias de cada valor en la columna de posiciones
position_counts = Counter(positions)

# Identificar valores duplicados
duplicates = [value for value, count in position_counts.items() if count > 1]

# Escribir en el archivo de texto con los datos ordenados
with open('<nombre del archivo>.txt', mode='w', encoding='utf-8') as file:
    if duplicates:
        file.write("Advertencia: Se encontraron valores de orden duplicados:\n")
        for value in duplicates:
            file.write(f"Valor duplicado: {value}\n")

    # Añadir los datos ordenados
    file.write("Elementos Ordenados:\n\n")
    sorted_rows = sorted(filtered_rows, key=lambda x: int(x[1]))
    for row in sorted_rows:
        # Suponemos que el nombre del elemento está en la primera columna (índice 0)
        # y el valor de orden en la segunda columna (índice 1)
        order_value = row[1]
        element_name = row[0]
        file.write(f"{order_value}. {element_name}\n")

print("El archivo ha sido ordenado y guardado como '<nombre del archivo>.txt'")
