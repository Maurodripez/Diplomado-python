class ErrorDeRango(Exception):
    def __init__(self):
        print("fuera de rango")


def readint(min, max):
    try:
        prompt = int(input("Ingresa un numero de -10 a 10: "))
        if prompt <= max and prompt >= min:
            return prompt
        elif prompt > max or prompt < min:
            raise ErrorDeRango()
    except ValueError:
        print("no es una cadena")
    except ErrorDeRango as e:
        print(e)


v = readint(-10, 10)

print("El numero es:", v)
