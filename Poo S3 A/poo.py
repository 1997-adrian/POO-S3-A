# ------------------------------------------------------------
# PROGRAMACIÓN ORIENTADA A OBJETOS: GESTIÓN DEL CLIMA SEMANAL
# ------------------------------------------------------------

class ClimaSemana:
    """
    Clase que modela el clima de una semana completa.
    
    Aplica el principio de **encapsulamiento**: los datos internos (temperaturas)
    están protegidos y solo se manipulan mediante métodos públicos.
    """
    
    # Atributo de clase: días de la semana (compartido por todas las instancias)
    DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def __init__(self):
        """
        Constructor de la clase.
        Inicializa una lista vacía para almacenar las temperaturas.
        El guion bajo en `_temperaturas` indica que es un atributo protegido.
        """
        self._temperaturas = []  # Lista protegida para almacenar temperaturas

    def ingresar_temperaturas(self):
        """
        Solicita al usuario las temperaturas para cada día de la semana.
        
        - Usa un bucle con validación de entrada (try/except).
        - Almacena cada valor válido en la lista protegida `_temperaturas`.
        """
        print("Ingrese las temperaturas diarias de la semana (en grados Celsius):")
        for dia in self.DIAS_SEMANA:
            while True:
                try:
                    temp = float(input(f"Temperatura del {dia}: "))
                    self._temperaturas.append(temp)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número (ej. 22.5).")

    def calcular_promedio(self):
        """
        Calcula el promedio semanal de las temperaturas almacenadas.
        
        - Retorna 0.0 si no hay datos (evita errores).
        - Usa la lista protegida `_temperaturas` para realizar el cálculo.
        """
        if not self._temperaturas:
            return 0.0
        return sum(self._temperaturas) / len(self._temperaturas)

    def mostrar_temperaturas(self):
        """
        Muestra las temperaturas diarias en un formato legible.
        
        - Itera sobre los días y las temperaturas simultáneamente.
        - Formatea cada valor a dos decimales para claridad.
        """
        if not self._temperaturas:
            print("⚠️  No hay temperaturas registradas.")
            return
        
        print("Temperaturas diarias:")
        for i, temp in enumerate(self._temperaturas):
            print(f"  {self.DIAS_SEMANA[i]}: {temp:.2f}°C")

    def mostrar_resumen(self):
        """
        Muestra un resumen completo: temperaturas diarias, promedio, mínima y máxima.
        
        - Esta función integra otros métodos para presentar una visión global.
        - Ilustra cómo los métodos internos colaboran entre sí.
        """
        if not self._temperaturas:
            print("⚠️  No hay datos para generar un resumen.")
            return
        
        print("\n🌤️  --- RESUMEN SEMANAL DEL CLIMA ---")
        self.mostrar_temperaturas()
        
        promedio = self.calcular_promedio()
        max_temp = max(self._temperaturas)
        min_temp = min(self._temperaturas)
        
        print(f"\n📊 Temperatura más alta: {max_temp:.2f}°C")
        print(f"📉 Temperatura más baja: {min_temp:.2f}°C")
        print(f"📈 Promedio semanal: {promedio:.2f}°C")


# ------------------------------------------------------------
# HERENCIA Y EXTENSIBILIDAD (OPCIONAL PERO DEMOSTRATIVA)
# ------------------------------------------------------------

class ClimaSemanaInternacional(ClimaSemana):
    """
    Clase derivada que extiende `ClimaSemana` para añadir funcionalidad internacional.
    
    - Hereda todos los métodos y atributos de la clase base.
    - Sobrescribe `mostrar_resumen()` para incluir unidades en Fahrenheit (polimorfismo).
    - Demuestra cómo la herencia permite reutilizar y especializar comportamientos.
    """
    
    def _celsius_a_fahrenheit(self, celsius):
        """Convierte una temperatura de Celsius a Fahrenheit."""
        return (celsius * 9/5) + 32

    def mostrar_resumen(self):
        """
        Versión sobrescrita del resumen que muestra temperaturas en ambas escalas.
        Esto es un ejemplo de **polimorfismo**: el mismo método se comporta de forma diferente.
        """
        if not self._temperaturas:
            print("⚠️  No hay datos para generar un resumen.")
            return
        
        print("\n🌍 --- RESUMEN SEMANAL (INTERNACIONAL) ---")
        print("Temperaturas diarias (Celsius / Fahrenheit):")
        for i, temp_c in enumerate(self._temperaturas):
            temp_f = self._celsius_a_fahrenheit(temp_c)
            print(f"  {self.DIAS_SEMANA[i]}: {temp_c:.2f}°C / {temp_f:.2f}°F")
        
        promedio_c = self.calcular_promedio()
        promedio_f = self._celsius_a_fahrenheit(promedio_c)
        max_c = max(self._temperaturas)
        min_c = min(self._temperaturas)
        
        print(f"\n📊 Máxima: {max_c:.2f}°C ({self._celsius_a_fahrenheit(max_c):.2f}°F)")
        print(f"📉 Mínima: {min_c:.2f}°C ({self._celsius_a_fahrenheit(min_c):.2f}°F)")
        print(f"📈 Promedio: {promedio_c:.2f}°C ({promedio_f:.2f}°F)")


# ------------------------------------------------------------
# FUNCIÓN PRINCIPAL Y EJECUCIÓN
# ------------------------------------------------------------

def main():
    """
    Función principal que permite elegir entre versiones del sistema de clima.
    
    - Para fines educativos, se usa la versión internacional (con herencia y polimorfismo).
    - Muestra cómo el diseño orientado a objetos facilita la extensión del código.
    """
    print("Sistema de Gestión del Clima Semanal (POO)")
    print("=========================================")
    
    # Se crea una instancia de la clase derivada para demostrar herencia y polimorfismo
    clima = ClimaSemanaInternacional()
    
    # Ingresar datos
    clima.ingresar_temperaturas()
    
    # Mostrar resumen (usará la versión sobrescrita gracias al polimorfismo)
    clima.mostrar_resumen()


# Punto de entrada del programa
if __name__ == "__main__":
    main()