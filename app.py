#Trabajo Practico Integrador 1
#Enrique Alejandro Juarez Alvarez/ Juan Martin Figuerero Amicone

import time
import random

def simular_puertas_logicas():
    a = int(input("Ingresa 0 o 1 para A: "))
    b = int(input("Ingresa 0 o 1 para B: "))
    print(f"\nAND: {a & b}")
    print(f"OR: {a | b}")
    print(f"NOT A: {int(not a)}")
    print(f"NOT B: {int(not b)}")
    print(f"NAND: {int(not (a & b))}")
    print(f"NOR: {int(not (a | b))}")
    print(f"XOR: {a ^ b}\n")

def conversion_numeros():
    opcion = input("¿Deseas convertir Decimal → Binario (1) o Binario → Decimal (2)? ")
    if opcion == '1':
        dec = int(input("Número decimal: "))
        print(f"Binario: {bin(dec)[2:]}")
    elif opcion == '2':
        binario = input("Número binario: ")
        try:
            print(f"Decimal: {int(binario, 2)}")
        except ValueError:
            print("Entrada inválida. Debe contener solo 0s y 1s.")

def contador_binario():
    print("Contando de 0 a 15 en binario:\n")
    for i in range(16):
        print(format(i, '04b'))
        time.sleep(0.5)

def tabla_verdad():
    operacion = input("Elige una operación (AND, OR, XOR): ").upper()
    print(f"\nTabla de verdad para A {operacion} B:")
    for A in [0,1]:
        for B in [0,1]:
            if operacion == "AND":
                resultado = A & B
            elif operacion == "OR":
                resultado = A | B
            elif operacion == "XOR":
                resultado = A ^ B
            else:
                print("Operación no válida.")
                return
            print(f"A={A}, B={B} => {resultado}")

def comparador_exp():
    expr1 = input("Primera expresión (ej. A and B): ")
    expr2 = input("Segunda expresión: ")
    combinaciones = [(0,0), (0,1), (1,0), (1,1)]
    iguales = True
    for A, B in combinaciones:
        res1 = eval(expr1)
        res2 = eval(expr2)
        print(f"A={A}, B={B} → {res1} == {res2}")
        if res1 != res2:
            iguales = False
    print("Las expresiones son equivalentes." if iguales else "Las expresiones NO son equivalentes.")

def operaciones_bit_a_bit():
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))
    print(f"AND: {a & b} ({bin(a & b)})")
    print(f"OR: {a | b} ({bin(a | b)})")
    print(f"XOR: {a ^ b} ({bin(a ^ b)})")

def sumador_1bit():
    a = int(input("Bit A (0 o 1): "))
    b = int(input("Bit B (0 o 1): "))
    suma = a ^ b
    carry = a & b
    print(f"Suma: {suma}, Carry: {carry}")

def juego_adivinanza():
    modo = input("¿Binario a decimal (1) o Decimal a binario (2)? ")
    if modo == '1':
        n = random.randint(0, 15)
        resp = int(input(f"¿Cuál es el decimal de {format(n, '04b')}? "))
        print("¡Correcto!" if resp == n else f"Incorrecto. Era {n}")
    elif modo == '2':
        n = random.randint(0, 15)
        resp = input(f"¿Cuál es el binario de {n}? ")
        print("¡Correcto!" if resp == format(n, '04b') else f"Incorrecto. Era {format(n, '04b')}")

def circuito_combinacional():
    binario = input("Ingresa un número binario de 4 bits: ")
    try:
        n = int(binario, 2)
        print("Es PAR" if n % 2 == 0 else "Es IMPAR")
    except ValueError:
        print("Entrada no válida. Usa solo 0 y 1.")

def menu():
    while True:
        print("\n📟 MENÚ PRINCIPAL - SIMULADOR LÓGICO 🔧")
        print("1. Simular puertas lógicas")
        print("2. Conversión de números")
        print("3. Contador binario")
        print("4. Generar tabla de verdad")
        print("5. Comparar expresiones booleanas")
        print("6. Calculadora bit a bit")
        print("7. Sumador de 1 bit")
        print("8. Juego de adivinanza binaria")
        print("9. Simulador de circuito combinacional")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1': simular_puertas_logicas()
        elif opcion == '2': conversion_numeros()
        elif opcion == '3': contador_binario()
        elif opcion == '4': tabla_verdad()
        elif opcion == '5': comparador_exp()
        elif opcion == '6': operaciones_bit_a_bit()
        elif opcion == '7': sumador_1bit()
        elif opcion == '8': juego_adivinanza()
        elif opcion == '9': circuito_combinacional()
        elif opcion == '0':
            print("¡Hasta luego, ingeniero del silicio!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el menú
menu()
