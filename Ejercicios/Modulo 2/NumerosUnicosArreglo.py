miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
listaAux=[]
cont=0;
for numero in miLista[:]:
    if numero not in miLista[numero+1:]:
        listaAux.extend([cont+1])
        listaAux[cont]=miLista[numero]
        cont+=1
miLista=listaAux
#
# coloca tu código aquí
#
print("La lista solo con elementos únicos:")
print(miLista)
