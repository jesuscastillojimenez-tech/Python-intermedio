"""
Sistema de evaluación

- Pide número de alumnos y número de materias.
- Para cada alumno pide: nombre  y matrícula.
- Para cada materia pide una calificación (0.0 - 10.0).
- Una calificación > 6 es APROBADO en esa materia; <= 6 es REPROBADO.
- El estado global del alumno (Aprobado/Reprobado) se decide por promedio:
    promedio > 6 -> Aprobado
    promedio <= 6 -> Reprobado
- Valida que no se dejen campos vacíos y que los números estén en rangos válidos.
"""

from typing import List, Dict, Tuple


def leer_entero_positivo(prompt: str) -> int:
    """Lee un entero positivo mayor que 0, repite hasta que sea válido."""
    while True:
        valor = input(prompt).strip()
        if valor == "":
            print("No puedes dejar el campo vacío. Ingresa un número.")
            continue
        try:
            n = int(valor)
            if n <= 0:
                print("El número debe ser mayor que 0. Intenta de nuevo.")
                continue
            return n
        except ValueError:
            print("Entrada inválida. Ingresa un número entero válido.")


def leer_cadena_no_vacia(prompt: str) -> str:
    """Lee una cadena no vacía; repite hasta que el usuario escriba algo distinto de espacios."""
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Este campo no puede quedar vacío. Intenta de nuevo.")
            continue
        return s


def leer_calificacion(prompt: str) -> float:
    """Lee una calificación numérica entre 0 y 10 (inclusive)."""
    while True:
        entrada = input(prompt).strip()
        if entrada == "":
            print("La calificación no puede estar vacía.")
            continue
        try:
            g = float(entrada)
            if g < 0 or g > 10:
                print("La calificación debe estar entre 0 y 10.")
                continue
            return g
        except ValueError:
            print("Entrada inválida. Ingresa un número (ej. 7,5 o 8).")


def procesar_estudiantes(num_alumnos: int, num_materias: int) -> Tuple[List[Dict], List[Dict]]:
    """
    Pide los datos de cada alumno y calcula su promedio y estado.
    Devuelve dos listas: (aprobados, reprobados) donde cada elemento es un dict con detalles.
    """
    aprobados = []
    reprobados = []

    for i in range(1, num_alumnos + 1):
        print(f"\n--- Alumno {i} de {num_alumnos} ---")
        nombre = leer_cadena_no_vacia("Nombre del alumno: ")
        matricula = leer_cadena_no_vacia("Matrícula: ")

        notas = []
        materias_pasadas = 0
        materias_reprobadas = 0

        for j in range(1, num_materias + 1):
            prompt = f"Calificación materia {j} (0-10) para {nombre}: "
            nota = leer_calificacion(prompt)
            notas.append(nota)
            # Evaluación por materia: >= 6 es aprobado
            if nota >= 6:
                materias_pasadas += 1
            else:
                materias_reprobadas += 1

        promedio = sum(notas) / len(notas)

        # Estado global: promedio >= 6 -> aprobado
        estado_global = "Aprobado" if promedio >= 6 else "Reprobado"

        # Guardamos un diccionario con la información del alumno
        info_alumno = {
            "nombre": nombre,
            "matricula": matricula,
            "notas": notas,
            "promedio": round(promedio, 2),
            "materias_aprobadas": materias_pasadas,
            "materias_reprobadas": materias_reprobadas,
            "estado": estado_global
        }

        if estado_global == "Aprobado":
            aprobados.append(info_alumno)
        else:
            reprobados.append(info_alumno)

    return aprobados, reprobados


def mostrar_reporte(aprobados: List[Dict], reprobados: List[Dict]) -> None:
    """Muestra por pantalla un resumen de aprobados y reprobados con detalles."""
    print("\n\n====== REPORTE FINAL ======\n")
    print(f"Total alumnos aprobados: {len(aprobados)}")
    if aprobados:
        print("\n--- Aprobados ---")
        for a in aprobados:
            print(f"Nombre: {a['nombre']} | Matrícula: {a['matricula']} | Promedio: {a['promedio']} | "
                  f"Materias aprobadas: {a['materias_aprobadas']} / {len(a['notas'])}")

    print(f"\nTotal alumnos reprobados: {len(reprobados)}")
    if reprobados:
        print("\n--- Reprobados ---")
        for r in reprobados:
            print(f"Nombre: {r['nombre']} | Matrícula: {r['matricula']} | Promedio: {r['promedio']} | "
                  f"Materias aprobadas: {r['materias_aprobadas']} / {len(r['notas'])}")

    print("\nDetalle completo de cada estudiante (notas por materia):")
    todos = aprobados + reprobados
    for t in todos:
        notas_str = ", ".join(str(n) for n in t["notas"])
        print(f"- {t['nombre']} ({t['matricula']}): Notas = [{notas_str}] | Promedio = {t['promedio']} | Estado = {t['estado']}")


def sistema_evaluacion():
    """Función principal: coordina la ejecución del sistema de evaluación."""
    print("Sistema de evaluación - registro de alumnos y cálculo de aprobados/reprobados")
    print("No se permiten campos vacíos. La regla de aprobación por materia: calificación > 6.\n")

    num_alumnos = leer_entero_positivo("Ingrese el número de alumnos: ")
    num_materias = leer_entero_positivo("Ingrese el número de materias: ")

    aprobados, reprobados = procesar_estudiantes(num_alumnos, num_materias)

    mostrar_reporte(aprobados, reprobados)


if __name__ == "__main__":
    sistema_evaluacion()
