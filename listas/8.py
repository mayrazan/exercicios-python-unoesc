idades = []
alturas = []
inversao_idade = []
inversao_altura = []

for i in range(0, 5):
    idade = int(input("Pessoa %d - Informe a idade: " % i))
    altura = float(input("Pessoa %d - Informe a altura: " % i))
    idades.append(idade)
    alturas.append(altura)
    
for a in reversed(idades):
    inversao_idade.append(a)

for b in reversed(alturas):
    inversao_altura.append(b)

print("Idades da lista: %r." % idades)
print("Alturas da lista: %r." % alturas)
print("Idade ordem inversa: %r" % inversao_idade)
print("Altura ordem inversa: %r" % inversao_altura)