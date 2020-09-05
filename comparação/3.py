sexo = input("Informe F para feminino ou M para masculino: ")

if sexo.upper() == "F":
    print("A letra %s - Feminino." % sexo.upper())
elif sexo.upper() == "M":
    print("A letra %s. - Masculino." % sexo.upper())
else:
    print("Sexo inválido.")

