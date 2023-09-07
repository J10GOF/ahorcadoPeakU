import random

palabras = ["python", "programacion", "juego", "diversion", "ordenador", "desarrollo", "inteligencia", "tecnologia", "computadora", "programador"]

def seleccionar_palabra():
    return random.choice(palabras)

def mostrar_palabra_adivinada(palabra_secreta, letras_adivinadas):
    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"
    return palabra_mostrada

def juego_ahorcado():
    palabra_secreta = seleccionar_palabra()
    intentos_maximos = 6
    intentos = 0
    letras_adivinadas = []

    print("¡Bienvenido al juego de Ahorcado!")
    print("Adivina la palabra secreta letra por letra.")
    print(f"Tienes un máximo de {intentos_maximos} intentos.")

    while intentos < intentos_maximos:
        palabra_actual = mostrar_palabra_adivinada(palabra_secreta, letras_adivinadas)
        print("\nPalabra actual: " + palabra_actual)

        if palabra_actual == palabra_secreta:
            print(f"\n¡Felicidades! Adivinaste la palabra secreta: {palabra_secreta}")
            break

        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Correcto! Esa letra está en la palabra.")
        else:
            intentos += 1
            print(f"Letra incorrecta. Te quedan {intentos_maximos - intentos} intentos restantes.")
            dibujar_ahorcado(intentos)

    if intentos == intentos_maximos:
        print(f"\nLo siento, te quedaste sin intentos. La palabra secreta era: {palabra_secreta}")

def dibujar_ahorcado(intentos):
    ahorcado = [
        """
           ------
           |    |
                |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        """
    ]
    print(ahorcado[intentos])

def main():
    while True:
        juego_ahorcado()
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != "s":
            break

    print("¡Gracias por jugar!")

if __name__ == "__main__":
    main()
