notas = []

for i in range(0, 4):
    nota = float(input("Informe uma nota: "))
    notas.append(nota)
    soma = sum(notas)
    media = soma / 4

print(notas)
print("A media das notas é: %f" % media)