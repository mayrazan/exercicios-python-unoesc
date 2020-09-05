listaA = []
soma = []
total = 0

for i in range(0, 10):
    lista = int(input("Informe um numero: "))
    listaA.append(lista)
    total += lista ** 2

for a in listaA:
    soma.append(a**2)

print("Lista de numeros informados: %r." % listaA)
print("A soma total dos quadrados de todos os elementos: %d " % total)
print("A soma de cada elemento quadrado: %r." % soma)