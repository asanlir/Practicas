"""
Calcula el crecimiento de una inversión durante un número determinado de años en base al capital
inicial, contribución anual, tipo de interés y número de años.

Tras solicitar los datos al usuario, la función calcula y muestra los resultados anuales del capital
inicial para ese año, beneficios obtenidos y capital obtenido.

Finalmente, imprime el resumen del importe total aportado, el total de intereses devengados, el
promedio anual de intereses y el capital total tras el número de años especificado.
"""

def calc_int():

    cap_ini = int(input("Indique su capital inicial: "))
    ap_anu = int(input("Indique la aportación anual: "))
    interes = float(input("Indique el interés de la cuenta (%): "))
    inte = interes / 100
    anualidades = int(input("¿Cuántos años quieres calcular?: "))
    cap = cap_ini + ap_anu  # Se suma la aportación inicial y la aportación del primer año
    total_aportado = cap_ini + ap_anu
    total_beneficios = 0
    print("\n")

    for i in range(anualidades):
        print(f"Capital base del año {i+1}: {cap:.2f}")

        # Calcular los intereses después de la aportación anual
        interes_ganado = cap * inte
        cap += interes_ganado
        total_beneficios += interes_ganado

        print(f"Interés ganado en el año {i+1}: {interes_ganado:.2f}")
        print(f"Capital después de intereses del año {i+1}: {cap:.2f}\n")

        # Añadir la aportación anual para el siguiente año, excepto en el último año
        if i < anualidades - 1:
            cap += ap_anu
            total_aportado += ap_anu

    print(f"Total aportado: {total_aportado:.2f}")
    print(f"Total beneficios generados por intereses: {total_beneficios:.2f}")
    print(f"Media de interés anual: {total_beneficios/anualidades:.2f}")
    print(f"Capital total después de {anualidades} años: {cap:.2f}")

calc_int()



while True:
    respuesta = input("\n¿Desea calcular otra vez? (s/n): ")
    if respuesta.lower() == "s":
        calc_int()
    else:
        break
