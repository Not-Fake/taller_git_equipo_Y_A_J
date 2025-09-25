# Taller Git  Y_A_J
# Integrantes: Yaider Martinez, Alan Orozco, Juan Pacheco

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b

def potencia(a, b):
    return a ** b

def menu():
    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("Saliendo del programa...")
            break

        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            print("Resultado:", dividir(a, b))
        elif opcion == "5":
            print("Resultado:", potencia(a, b))
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
