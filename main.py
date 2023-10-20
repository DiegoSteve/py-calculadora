from calculadora import Calculadora

def main():
    calc = Calculadora()

    while True:
        print("Opciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Elige una opción (1/2/3/4/5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion in ("1", "2", "3", "4"):
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if opcion == "1":
                resultado = calc.suma(num1, num2)
                operacion = "suma"
            elif opcion == "2":
                resultado = calc.resta(num1, num2)
                operacion = "resta"
            elif opcion == "3":
                resultado = calc.multiplicacion(num1, num2)
                operacion = "multiplicación"
            elif opcion == "4":
                resultado = calc.division(num1, num2)
                operacion = "división"

            print(f"El resultado de la {operacion} es: {resultado}\n")
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main":
    main()
