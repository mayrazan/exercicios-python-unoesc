listaA = []
listaB = []
listaC = []

for i in range(0, 10):
    lista1 = int(input("Informe um numero para a lista A: "))
    lista2 = int(input("Informe um numero para a lista B: "))
    listaA.append(lista1)
    listaB.append(lista2)

    listaC.append(listaA[i])
    listaC.append(listaB[i])

print("Lista de numeros informados: %r." % listaC)