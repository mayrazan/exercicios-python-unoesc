numeros = []
par = []
impar = []


for i in range(0, 5):
    numero = int(input("Informe um numero: "))
    numeros.append(numero)
    resto = numero % 2

    if resto == 0: 
        par.append(numero)  
    else:
        impar.append(numero)

print(numeros)
print("Numeros pares: %r" % par)
print("Numeros impares: %r" % impar)