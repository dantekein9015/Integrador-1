#Trabajo Practico Integrador 1
#Enrique Alejandro Juarez Alvarez / Juan Martin Figuerero Amicone

def decimal_a_binario(numero):
    return bin(numero)[2:]

def binario_a_decimal(bin_str):
    try:
        return int(bin_str, 2)
    except ValueError:
        return None

def menu():
    print("🔢 Conversor Decimal ↔ Binario")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            try:
                num = int(input("Ingrese un número decimal: "))
                binario = decimal_a_binario(num)
                print(f"✅ Binario: {binario}\n")
            except ValueError:
                print("❌ Error: ingrese un número entero.\n")

        elif opcion == "2":
            bin_str = input("Ingrese un número binario (solo 0 y 1): ")
            decimal = binario_a_decimal(bin_str)
            if decimal is not None:
                print(f"✅ Decimal: {decimal}\n")
            else:
                print("❌ Error: valor no válido como número binario.\n")

        elif opcion == "3":
            print("👋 Hasta luego.")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()
