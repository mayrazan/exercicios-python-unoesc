numeros = []
soma = 0
multiplicacao = 1

for i in range(0, 5):
    numero = int(input("Informe um numero: "))
    numeros.append(numero)
    soma += numero
    multiplicacao *= numero

print("Numeros da lista: %r." % numeros)
print("Soma dos numeros: %d." % soma)
print("Multiplicação dos numeros: %d." % multiplicacao)