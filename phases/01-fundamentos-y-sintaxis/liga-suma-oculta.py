"""
Solucion del reto de la fase 1
Ejecutar: python phases/01-fundamentos-y-sintaxis/liga-suma-oculta.py
"""

import random
rondas = 0
rondas_ganadas = 0
rondas_perdidas = 0
total_intentos = 0

name = None
while name is None or name.strip() == "":
    name = input("Ingrese su nombre: ")
print(f"Bienvenido {name}")

# Jugar una partida
def jugar_partida(name):
    global rondas
    global rondas_ganadas
    global rondas_perdidas
    global total_intentos

    # Solicitar dificultad Fácil, Media, Difícil
    while True:
        print("Dificultad:")
        print("1. Fácil")
        print("2. Media")
        print("3. Difícil")
        dificultad = input("Ingrese una dificultad: ")
        if dificultad.strip() == "1":
            Max = 10
            Tries = 5
            break
        elif dificultad.strip() == "2":
            Max = 25
            Tries = 7
            break
        elif dificultad.strip() == "3":
            Max = 50
            Tries = 10
            break
        else:
            print("Dificultad no válida")
            continue

    # Solicitar cuántas rondas se jugarán
    while True:
        rondas_texto = input("Ingrese la cantidad de rondas: ")
        if not rondas_texto.isdigit() or int(rondas_texto) < 1:
            print("Cantidad de rondas no válida, debe ser un número entero mayor a 0")
            continue
        rondas = int(rondas_texto)
        break
    
    # En cada ronda:
    for ronda in range(rondas):
        print(f"Ronda {ronda + 1} de {rondas}")
        # Generar dos secretos aleatorios
        secretos = [random.randint(1, Max) for _ in range(2)]
        suma_secreta = sum(secretos)
        print(f"La suma de los secretos está entre {2} y {2*Max}")
        # En cada intento, el jugador propone un entero (supuesta suma). Si no coincide, indica si la suma real es **mayor** o **menor** que la propuesta. Si coincide, la ronda se gana.
        for t in range(Tries):
            propuesta = input("Ingrese una propuesta: ")
            # validar que sea un numero entero
            if not propuesta.isdigit() or int(propuesta) < 1:
                print("La propuesta no es un número entero")
                continue
            propuesta = int(propuesta)
            if propuesta == suma_secreta:
                print("Has ganado la ronda")
                rondas_ganadas += 1
                break
            elif propuesta > suma_secreta:
                print(f"La suma real es menor te quedan {Tries - t - 1} intentos")
            else:
                print(f"La suma real es mayor te quedan {Tries - t - 1} intentos")

            total_intentos += 1
        if propuesta != suma_secreta:
            print("Has perdido la ronda")
            rondas_perdidas += 1
        rondas += 1
        continue
    

def ver_estadisticas():
    global rondas
    global rondas_ganadas
    global rondas_perdidas
    global total_intentos
    print(f"rondas jugadas: {rondas}")
    print(f"Rondas ganadas: {rondas_ganadas}")
    print(f"Rondas perdidas: {rondas_perdidas}")
    if rondas == 0:
        print("No hay rondas jugadas")
        return
    print(f"Promedio de intentos: {total_intentos / rondas}")

# Menú principal
while True:
    print("1. Jugar una partida")
    print("2. Ver estadisticas")
    print("3. Modo entrenador")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion.strip() == "1":
        print("Jugar una partida")
        jugar_partida(name)
    elif opcion.strip() == "2":
        print("Ver estadisticas")
        ver_estadisticas()
    elif opcion.strip() == "3":
        print("Modo entrenador")
        modo_entrenador(name)
    elif opcion.strip() == "4":
        print("Salir")
        break
    else:
        print("Opcion no valida")
    continue
