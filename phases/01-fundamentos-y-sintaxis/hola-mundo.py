"""
Ejecutar: python phases/01-fundamentos-y-sintaxis/hola-mundo.py
"""

print("Hola mundo")

nombre = None
while nombre is None or nombre.strip() == "":
    nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

especie = None
while especie is None or especie.strip() == "":
    especie = input("Ingrese su especie: ")
print(f"Hola {nombre} de la especie {especie}")

edad = None
while edad is None or edad.strip() == "":
    edad = input("Ingrese su edad: ")
    if not edad.isdigit() or int(edad) < 0:
        print("La edad no es un número entero mayor a 0")
        continue
    edad = int(edad)
    break
print(f"Hola {especie} de {edad} años llamado {nombre}")