def solicitar_rentero():
    # Solicita al usuario que ingrese un número entero
    while True:
        try:
            rentero = int(input("Ingrese un número entero: "))
            return rentero
        except ValueError:
            print("Por favor, ingrese un valor válido.")

def mostrar_cuadrado(rentero):
    # Calcula y muestra el cuadrado del número ingresado
    cuadrado = rentero ** 2
    print(f"El cuadrado de {rentero} es: {cuadrado}")

# Ejemplo de uso
rentero = solicitar_rentero()  # Llama a la función para solicitar el entero
mostrar_cuadrado(rentero)      # Llama a la función para mostrar el cuadrado
