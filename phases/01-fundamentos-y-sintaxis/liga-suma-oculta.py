"""
Solucion del reto de la fase 1.
Ejecutar: python phases/01-fundamentos-y-sintaxis/liga-suma-oculta.py
"""

import random
import sys

partidas_jugadas = 0
rondas_jugadas = 0
rondas_ganadas = 0
rondas_perdidas = 0
total_intentos = 0


def pedir_nombre():
    nombre = None
    while nombre is None or nombre.strip() == "":
        nombre = input("Ingrese su nombre: ")
    return nombre.strip()


def pedir_entero_positivo(mensaje):
    while True:
        valor_texto = input(mensaje).strip()
        if not valor_texto.isdigit() or int(valor_texto) < 1:
            print("Debe ingresar un numero entero mayor a 0.")
            continue
        return int(valor_texto)


def obtener_configuracion_dificultad():
    while True:
        print("Dificultad:")
        print("1. Facil")
        print("2. Media")
        print("3. Dificil")
        dificultad = input("Ingrese una dificultad: ").strip()

        if dificultad == "1":
            return 10, 5, "Facil"
        if dificultad == "2":
            return 25, 7, "Media"
        if dificultad == "3":
            return 50, 10, "Dificil"

        print("Dificultad no valida.")


def jugar_partida(nombre):
    global partidas_jugadas
    global rondas_jugadas
    global rondas_ganadas
    global rondas_perdidas
    global total_intentos

    maximo_secreto, intentos_maximos, nombre_dificultad = obtener_configuracion_dificultad()
    total_rondas = pedir_entero_positivo("Ingrese la cantidad de rondas: ")
    partidas_jugadas += 1

    print(f"\n{nombre} inicia una partida en dificultad {nombre_dificultad}.\n")

    for numero_ronda in range(1, total_rondas + 1):
        secretos = [random.randint(1, maximo_secreto), random.randint(1, maximo_secreto)]
        suma_secreta = sum(secretos)
        acertado = False
        intentos_ronda = 0

        print(f"Ronda {numero_ronda} de {total_rondas}")
        print(f"La suma de los secretos esta entre 2 y {2 * maximo_secreto}.")

        while intentos_ronda < intentos_maximos and not acertado:
            propuesta = input("Ingrese una propuesta: ").strip()
            if not propuesta.isdigit() or int(propuesta) < 1:
                print("La propuesta debe ser un numero entero mayor a 0.")
                continue

            propuesta = int(propuesta)
            intentos_ronda += 1

            if propuesta == suma_secreta:
                print("Has ganado la ronda.")
                acertado = True
            elif propuesta > suma_secreta:
                print(f"La suma real es menor. Intentos restantes: {intentos_maximos - intentos_ronda}")
            else:
                print(f"La suma real es mayor. Intentos restantes: {intentos_maximos - intentos_ronda}")

        rondas_jugadas += 1
        total_intentos += intentos_ronda

        if acertado:
            rondas_ganadas += 1
        else:
            rondas_perdidas += 1
            print("Has perdido la ronda.")

        print(f"Desenlace: los secretos eran {secretos[0]} y {secretos[1]}.\n")


def ver_estadisticas():
    print(f"Partidas jugadas: {partidas_jugadas}")
    print(f"Rondas jugadas: {rondas_jugadas}")
    print(f"Rondas ganadas: {rondas_ganadas}")
    print(f"Rondas perdidas: {rondas_perdidas}")

    if rondas_jugadas == 0:
        print("Promedio de intentos: 0.0")
        return

    print(f"Promedio de intentos: {total_intentos / rondas_jugadas:.2f}")


def modo_entrenador(nombre):
    mensaje = f"Jugador: {nombre} | Rondas jugadas: {rondas_jugadas} | Rondas ganadas: {rondas_ganadas}"
    print(mensaje)
    print(f"Tamanio aproximado de la cadena: {sys.getsizeof(mensaje)} bytes")


name = pedir_nombre()
print(f"Bienvenido {name}")

# Menu principal
while True:
    print("\n1. Jugar una partida")
    print("2. Ver estadisticas")
    print("3. Modo entrenador")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ").strip()

    if opcion == "1":
        jugar_partida(name)
    elif opcion == "2":
        ver_estadisticas()
    elif opcion == "3":
        modo_entrenador(name)
    elif opcion == "4":
        print("Salir")
        break
    else:
        print("Opcion no valida")
