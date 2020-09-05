numero1 = int(input("Informe o primeiro numero: "))
numero2 = int(input("Informe o segundo numero: "))
numero3 = int(input("Informe o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("Maior numero: %d." %numero1)
elif numero2 > numero1 and numero2 > numero3:
  	print("Maior numero: %d." % numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("Maior numero: %d." % numero3)