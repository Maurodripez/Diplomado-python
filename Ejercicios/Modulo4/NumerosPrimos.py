def NumeroPrimo(num):
    cont=0
    for i in range(1,20):
        if num % i == 0:
            cont+=1
    if cont <=2:
        print("es numero primo")
    else:
        print("no es primo")
NumeroPrimo(18)
