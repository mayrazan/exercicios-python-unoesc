letra = input("Informe uma letra: ")

if letra.upper() == "A" or letra.upper() == "E" or letra.upper() == "I" or letra.upper() == "O" or letra.upper() == "U":
    print("A letra %s é uma vogal." % letra.upper())
else:
    print("A letra %s é uma consoante." % letra)
