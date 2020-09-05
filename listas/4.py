caracteres = []
cont = 0
vogais = 0

for i in range(0, 10):
    letra = input("Informe uma letra: ")
    caracteres.append(letra)
    
    if letra in 'aeiou': 
        vogais += 1
        caracteres.remove(letra)
    else:
        cont += 1

print("Foram lidas %d consoantes" % cont)
print(caracteres)