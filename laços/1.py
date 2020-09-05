nota = float(input("Informe uma nota: "))

while nota > 10 or nota < 0:
    print("Valor invalido, tente novamente.")
    
    nota = float(input("Informe uma nota: "))

if nota <= 10:
    print("Nota informada: {:.2f}." .format(nota))