# ------------------------------------------------------------
# PROGRAMACIÓN TRADICIONAL: GESTIÓN DE TEMPERATURAS SEMANALES
# ------------------------------------------------------------

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas de los 7 días de la semana.
    
    - Usa una lista predefinida con los nombres de los días para guiar al usuario.
    - Valida que cada entrada sea un número válido (manejo de errores con try/except).
    - Retorna una lista de 7 temperaturas en formato flotante.
    """
    # Lista con los nombres de los días de la semana para referencia
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []  # Lista vacía para almacenar las temperaturas ingresadas

    print("Por favor, ingrese las temperaturas diarias de la semana (en grados Celsius):")
    
    # Bucle que recorre cada día de la semana
    for dia in dias:
        while True:  # Bucle para reintentar si la entrada no es válida
            try:
                # Solicita al usuario la temperatura del día actual
                temp = float(input(f"Temperatura del {dia}: "))
                temperaturas.append(temp)  # Agrega la temperatura a la lista
                break  # Sale del bucle si la entrada es válida
            except ValueError:
                # Si el usuario ingresa un valor no numérico, muestra un mensaje de error
                print("Entrada inválida. Por favor, ingrese un número (por ejemplo: 23.5).")
    
    return temperaturas  # Devuelve la lista completa de temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    
    - Verifica que la lista no esté vacía para evitar errores de división por cero.
    - Retorna el promedio como un número flotante.
    """
    if len(temperaturas) == 0:
        # Si no hay datos, devuelve 0 para evitar errores
        return 0.0
    # Calcula la suma de todas las temperaturas y la divide entre el número de días
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


def main():
    """
    Función principal que organiza el flujo del programa.
    
    - Llama a la función para ingresar temperaturas.
    - Calcula el promedio semanal.
    - Muestra los resultados al usuario de forma clara y formateada.
    """
    # Paso 1: Ingresar las temperaturas de la semana
    temperaturas_semana = ingresar_temperaturas()
    
    # Paso 2: Calcular el promedio semanal
    promedio_semanal = calcular_promedio(temperaturas_semana)
    
    # Paso 3: Mostrar los resultados
    print("\n--- Resultados ---")
    print("Temperaturas ingresadas:")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for i in range(7):
        print(f"  {dias[i]}: {temperaturas_semana[i]:.2f}°C")
    
    print(f"\n✅ Promedio semanal de temperaturas: {promedio_semanal:.2f}°C")


# Punto de entrada del programa
if __name__ == "__main__":
    # Esta condición asegura que el código solo se ejecute si el script se corre directamente
    main()