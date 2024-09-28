def contar_a(cadena):
    # Inicializa el contador
    contador = 0
    
    # Recorre cada carácter en la cadena
    for caracter in cadena:
        # Verifica si el carácter es 'a' o 'A'
        if caracter == 'a' or caracter == 'A':
            contador += 1
            
    return contador
