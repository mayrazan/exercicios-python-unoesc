nome = input("Informe um nome: ")
idade = int(input("Informe uma idade: "))
salario = float(input("Informe salario: "))
sexo = input("Informe sexo: ")
estado_civil = input("Informe estado civil: ")


if len(nome) > 3:
    print("Seu nome é: %s." % nome)
else:
    print("Nome deve possuir mais que três caracteres.")

if idade > 0 and idade < 150:
    print("A sua idade é: %d." % idade)
else:
    print("Idade deve ser entre 0 e 150.")

if salario > 0:
    print("Seu salario é: {:.2f}" .format(salario))
else:
    print("Salario deve ser maior que 0.")

if sexo.lower() == "f" or sexo.lower() == "m":
    print("Sexo é: %s." % sexo)
else:
    print("Sexo deve ser 'f' ou 'm'.")

if estado_civil.lower() == 's' or estado_civil.lower() == 'c' or estado_civil.lower() == 'v' or estado_civil.lower() == 'd':
    print("Seu estado civil é: %s." % estado_civil)
else:
    print("Caractere inválido.")