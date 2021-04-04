cadenaInicial=input("introduce el mensaje a encriptar")
desplazamiento=int(input("introduce el desplazamiento"))
cifrado=''
for i in cadenaInicial:
    print(ord(i)+desplazamiento)
    if ord(i)==32 or (ord(i)>=48 and ord(i)<=59):
        codigo=ord(i)
    elif (ord(i)+desplazamiento)>90 and (ord(i)+desplazamiento)<=90+desplazamiento:
        codigo = (ord('A') + desplazamiento)-(-ord(i)+91)
    elif (ord(i)+desplazamiento)>122:
        codigo = (ord('a') + desplazamiento)-(123-ord(i))
    elif ord(i)==90:
        codigo = ord('A')+ (desplazamiento-1)
    elif ord(i)>=122 or (ord(i)+desplazamiento)>122:
        codigo = ord('a')+(desplazamiento-1)
    else:
        codigo = ord(i) + desplazamiento
    cifrado+=chr(codigo)
print(cifrado)
