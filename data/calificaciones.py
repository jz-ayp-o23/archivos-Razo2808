# Función para calcular el promedio de una lista de calificaciones
def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 1)

# Abrir el archivo de entrada con las calificaciones
with open('data/calificaciones.txt', 'r') as archivo_entrada:
    # Abrir el archivo de salida para escribir los resultados
    with open('data/promedios.txt', 'w') as archivo_salida:
        for linea in archivo_entrada:
            # Dividir la línea en palabras separadas por espacios
            palabras = linea.split()
            
            # Obtener el apellido y el nombre del estudiante
            apellido = palabras[1]
            nombre = palabras[0]
            
            # Obtener las calificaciones como una lista de números
            calificaciones = [float(cal) for cal in palabras[2:]]
            
            # Calcular el promedio de las calificaciones
            promedio = calcular_promedio(calificaciones)
            
            # Escribir el resultado en el archivo de salida en el formato deseado
            archivo_salida.write(f'{apellido.upper()}, {nombre}: {promedio}\n')

print("Proceso completado. Los resultados se han guardado en data/promedios.txt")