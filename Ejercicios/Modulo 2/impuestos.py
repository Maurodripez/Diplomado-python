ingreso = float(input("Ingrese el ingreso anual:"))

if ingreso < 85528:
    print("excepcion fiscal")
    impuesto = (ingreso*.18)-556
    if impuesto < 0:
        print("El impuesto es: ", 0, "pesos")
    else:
        print("El impuesto es: ", impuesto, "pesos")
elif ingreso >= 85528:
    impuesto = 14839+(ingreso*.32)
    impuesto = round(impuesto, 0)
    print("El impuesto es: ", impuesto, "pesos")
