ano = int(input("introduce un ano"))
if(ano < 1582):
    print("no dentro del periodo del calendario gregoriano")
elif (ano % 4):
    print("es ano comun")
elif (ano % 100):
    print("es ano bisiesto")
elif (ano % 400):
    print("es ano comun")
elif(ano < 1582):
    print("no dentro del periodo del calendario gregoriano")
else:
    print("es un ano bisiesto")
