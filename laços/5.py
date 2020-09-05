paisA = int(input("Informe o numero da população A: "))
paisB = int(input("Informe o numero da população B: "))
taxaA = float(input("Informe a taxa da população A: "))
taxaB = float(input("Informe a taxa da população B: "))
ano = 0

while paisA < paisB:
    paisA = paisA + (paisA * (taxaA / 100))
    paisB = paisB + (paisB * (taxaB / 100))
    ano = ano + 1

    if paisA >= paisB:
        print("A população do País A deve ultrapassar ou igualar a população do País B em %d anos." % ano)

        ano = 0
        paisA = int(input("Informe o numero da população A: "))
        paisB = int(input("Informe o numero da população B: "))
        taxaA = float(input("Informe a taxa da população A: "))
        taxaB = float(input("Informe a taxa da população B: "))

while paisA > paisB:
    paisA = paisA + (paisA * (taxaA / 100))
    paisB = paisB + (paisB * (taxaB / 100))
    ano = ano + 1

    if paisA <= paisB:
        print("A população do País B deve ultrapassar ou igualar a população do País A em %d anos." % ano)

        ano = 0
        paisA = int(input("Informe o numero da população A: "))
        paisB = int(input("Informe o numero da população B: "))
        taxaA = float(input("Informe a taxa da população A: "))
        taxaB = float(input("Informe a taxa da população B: "))