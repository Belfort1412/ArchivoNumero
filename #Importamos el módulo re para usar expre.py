#Importamos el módulo re para usar expresiones regulares
import re

# Abrimos el archivo de entrada en modo de lectura
f = open("ArchivoNumero.txt", "r")

# Leemos todas las líneas del archivo y las guardamos en una variable
lineas = f.readlines()

# Creamos una lista vacía para almacenar los números
numeros = []

# Recorremos cada línea del archivo
for linea in lineas:
    # Usamos una expresión regular para encontrar todos los números en la línea
    # La expresión regular \d+ significa una o más cifras
    # La función re.findall devuelve una lista de todas las coincidencias
    numeros_en_linea = re.findall("\d+", linea)

    # Convertimos cada número a entero y lo agregamos a la lista de números
    for numero in numeros_en_linea:
        numeros.append(int(numero))

# Cerramos el archivo de entrada
f.close()

# Ordenamos la lista de números de forma ascendente
# Si quieres ordenarla de forma descendente, usa el argumento reverse=True
numeros.sort()

# Abrimos el archivo de salida en modo de escritura
g = open("ArchivoOrdenado.txt", "w")

# Recorremos la lista de números ordenados
for numero in numeros:
    # Escribimos cada número en el archivo de salida, seguido de un salto de línea
    # Usamos la función str para convertir el número a cadena
    g.write(str(numero) + "\n")

# Cerramos el archivo de salida
g.close()
