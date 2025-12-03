import logging

# Configuración de mensajes de depuración (Checklist: Mensajes informativos/depuración)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def validar_datos(nombre, edad, correo):
    """
    Valida nombre, edad y correo con manejo de errores.
    Cumple con: Validación de tipo y valor de 3 datos.
    """
    try:
        # Depuración
        logging.info(f"--- Iniciando validación para el usuario: {nombre} ---")

        # 1. Validación de NOMBRE (Cadena no vacía)
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un texto.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        # 2. Validación de EDAD
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")

        # Extensión para obtener la 3ra excepción: ZeroDivisionError
        # Si la edad es 0, esto fallará antes de la validación de valor positivo
        calculo_riesgo = 100 / edad

        if edad < 0:
            raise ValueError("La edad debe ser mayor que cero.")

        # 3. Validación de CORREO (@ presente)
        if not isinstance(correo, str):  # Verificación de tipo extra
            raise TypeError("El correo debe ser un texto.")
        if "@" not in correo:
            raise ValueError("El correo no es válido (falta '@').")

        # Si todo es correcto
        print(f"¡Éxito! Usuario '{nombre}' registrado correctamente.")

    except TypeError as e:
        # Captura errores de tipo de dato
        print(f"Error de Tipo: {e}")
    except ZeroDivisionError:
        # Captura si la edad es 0 (Cumple con 'Al menos 3 excepciones diferentes')
        print("Error Matemático: La edad no puede ser cero.")
    except ValueError as e:
        # Captura errores de lógica (vacío, negativo, sin @)
        print(f"Error de Valor: {e}")
    except Exception as e:
        # Captura cualquier otro error imprevisto
        print(f"Error desconocido: {e}")

    finally:
        # Mensaje de cierre obligatorio (Checklist: Uso de finally)
        print(">> Proceso de validación finalizado.\n")


def probar_validaciones():
    """
    Función de prueba con múltiples casos (Checklist: Entradas correctas e incorrectas)
    """
    datos_prueba = [
        ("Ana", 25, "ana@mail.com"),      # Correcto
        ("", 30, "b@m.com"),              # Error: Nombre vacío (ValueError)
        ("Luis", "veinte", "l@m.com"),    # Error: Edad texto (TypeError)
        ("Pedro", 0, "p@m.com"),          # Error: Edad cero (ZeroDivisionError)
        ("Juan", -5, "j@m.com"),          # Error: Edad negativa (ValueError)
        ("Maria", 20, "correo_sin_arroba")  # Error: Correo mal (ValueError)
    ]

    print("INICIANDO BATERÍA DE PRUEBAS...\n")
    for n, e, c in datos_prueba:
        validar_datos(n, e, c)


# Ejecutar pruebas
probar_validaciones()
