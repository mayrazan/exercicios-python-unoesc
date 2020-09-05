numero1 = input("Informe um número: ")
numero2 = input("Informe um número: ")

if numero1 > numero2:
    print("O maior numero é %s." % numero1)
elif numero1 < numero2:
    print("O maior numero é %s." % numero2)
elif numero1 == numero2:
    print("O numero %s e o numero %s são iguais." % (numero1, numero2))