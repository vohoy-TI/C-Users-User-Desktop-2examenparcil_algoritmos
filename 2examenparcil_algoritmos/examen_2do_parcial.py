# Solicita al usuario que ingrese un correo electrónico
mail = input("Ingrese un mail: ")

# Inicializa variables
cantidad = 0
x = 0

# Recorre el correo electrónico
while x < len(mail):
    if mail[x] == "@":  # Cambié "=" por "=="
        cantidad += 1
    x += 1  # Cambié "x=x++1" por "x += 1"

# Verifica la cantidad de caracteres "@"
if cantidad == 1:
    print("Contiene solo un caracter '@' el mail ingresado.")
else:
    print("Incorrecto")
