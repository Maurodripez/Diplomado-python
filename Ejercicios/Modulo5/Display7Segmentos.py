uno=[[" "," ","#"],[" "," ","#"],[" "," ","#"],[" "," ","#"],[" "," ","#"]]
dos=["#","#","#"],[" "," ","#"],["#","#","#"],["#"," "," "],["#","#","#"]
tres=["#","#","#"],[" "," ","#"],["#","#","#"],[" "," ","#"],["#","#","#"]
cuatro=["#"," ","#"],["#"," ","#"],["#","#","#"],[" "," ","#"],[" "," ","#"]
cinco=["#","#","#"],["#"," "," "],["#","#","#"],[" "," ","#"],["#","#","#"]
seis=["#","#","#"],["#"," "," "],["#","#","#"],["#"," ","#"],["#","#","#"]
siete=["#","#","#"],[" "," ","#"],[" "," ","#"],[" "," ","#"],[" "," ","#"]
ocho=["#","#","#"],["#","#","#"],["#","#","#"],["#","#","#"],["#","#","#"]
nueve=["#","#","#"],["#"," ","#"],["#","#","#"],[" "," ","#"],[" "," ","#"]
numero=[uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve]
x=int(input("introduce el numero que quieres visualizar"))
numeroAsignado=numero[x-1]

for i in range(len(numeroAsignado)):
    for j in range(len(numeroAsignado[i])):
        print(numeroAsignado[i][j], end=" ")
    print()
