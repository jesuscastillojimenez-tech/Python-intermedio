"""
Calculadora de edad.

Comportamiento:
- Si el usuario ingresa 29-02 en un año no bisiesto, muestra en la misma línea:
    Fecha errónea, pero se muestra la edad: 
  y luego continúa.
- Si el año es bisiesto, acepta 29-02 normalmente.
- Mantiene todas las demás validaciones (campo vacío, año > 1900, etc.)
"""


from datetime import date


def es_bisiesto(y: int) -> bool:
    """Devuelve True si el año y es bisiesto."""
    return (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)


def leer_fecha_input(texto_prompt="Ingresa fecha (DD-MM-AAAA) o 'salir': "):
    entrada = input(texto_prompt).strip()
    if entrada.lower() == "salir":
        return None
    if entrada == "":
        print("Error: no se puede dejar el campo vacío.")
        return False

    partes = entrada.split("-")
    if len(partes) != 3:
        print("Error: formato inválido. Usa DD-MM-AAAA (por ejemplo 05-09-1990).")
        return False

    try:
        d = int(partes[0])
        m = int(partes[1])
        y = int(partes[2])
    except ValueError:
        print("Error: la fecha debe contener solo números en formato DD-MM-AAAA.")
        return False

    return (d, m, y)


def calcular_edad_y_cumple(fecha_nac: date):
    hoy = date.today()
    edad = hoy.year - fecha_nac.year

    if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
        edad -= 1
        cumplio = False
        cumple_hoy = False
    elif (hoy.month, hoy.day) == (fecha_nac.month, fecha_nac.day):
        cumplio = True
        cumple_hoy = True
    else:
        cumplio = True
        cumple_hoy = False

    return edad, cumplio, cumple_hoy


def calculadora_edad():
    print("Calculadora de edad - Ingrese la fecha de nacimiento en formato DD-MM-AAAA.")
    print("Escribe 'salir' para terminar.\n")

    while True:
        resultado = leer_fecha_input()
        if resultado is None:
            print("Saliendo de la calculadora de edad.")
            break
        if resultado is False:
            continue

        d, m, y = resultado

        # Validaciones básicas
        if y <= 1900:
            print("El año de nacimiento debe ser mayor a 1900.")
            continue

        hoy = date.today()

        # Manejo especial para 29 de febrero
        nota_29feb = ""
        fecha_ajustada = False
        if d == 29 and m == 2:
            if es_bisiesto(y):
                # Año de nacimiento bisiesto: fecha válida
                fecha_nac = date(y, 2, 29)
                nota_29feb = "Nota: Naciste el 29 de febrero (cumples cada 4 años xD)."
            else:
                # Año no bisiesto: calcular usando 28/02 pero mostrar el mensaje inmediato con la edad
                try:
                    # usar 28-feb para calcular la edad
                    fecha_nac = date(y, 2, 28)
                    fecha_ajustada = True
                except ValueError:
                    print(
                        "Error inesperado al ajustar la fecha 28-02. Intenta de nuevo.")
                    continue
        else:
            # Validación normal de fecha existente (maneja días por mes y bisiestos)
            try:
                fecha_nac = date(y, m, d)
            except ValueError:
                print(
                    "Fecha inválida (día/mes no corresponden o valores fuera de rango).")
                continue

        # No permitir fechas futuras (comparar con la fecha final usada para cálculo)
        if fecha_nac > hoy:
            print("La fecha de nacimiento no puede ser futura.")
            continue

        # Calcular edad y estado de cumpleaños
        edad, cumplio, cumple_hoy = calcular_edad_y_cumple(fecha_nac)

        # Si fue 29/02 en año no bisiesto, mostrar la línea exacta con la edad inmediatamente
        if fecha_ajustada:
            print(f"Fecha errónea, pero se muestra la edad: {edad} años")

        # Luego mostramos la nota si aplica y el resto de la información
        if nota_29feb:
            print(nota_29feb)

        if fecha_ajustada:
            print("Nota: se usó 28-02 para el cálculo por 29-02 en año no bisiesto.")

        if cumple_hoy:
            print(f"¡Feliz cumpleaños! Hoy cumple {edad} años.")
        else:
            if cumplio:
                print(
                    f"El cliente tiene {edad} años y ya cumplió años este año.")
            else:
                print(
                    f"El cliente tiene {edad} años y aún no ha cumplido años este año.")

        if fecha_ajustada:
            print(
                f"Fecha de nacimiento registrada (ajustada para cálculo): {fecha_nac.strftime('%d-%m-%Y')}")
        else:
            print(
                f"Fecha de nacimiento registrada: {fecha_nac.strftime('%d-%m-%Y')}")
        print(f"Edad calculada: {edad}\n")


if __name__ == "__main__":
    calculadora_edad()
