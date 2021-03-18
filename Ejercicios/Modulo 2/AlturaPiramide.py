bloques = int(input("Ingrese el número de bloques:"))
nivel=1
while bloques>nivel:
    bloques=bloques-nivel
    nivel+=1
    if nivel > bloques:
        nivel+=-1
        break
    print("nivel: ",nivel," Bloques: ",bloques)
#
# Escribe tu código aquí.
#
print("La altura de la pirámide:", nivel)
