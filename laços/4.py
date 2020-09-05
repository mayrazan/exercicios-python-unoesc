paisA = 80000
paisB = 200000
taxaA = 3 / 100
taxaB = 1.5 / 100
ano = 0

while paisA < paisB:
    paisA = paisA + (paisA * taxaA)
    paisB = paisB + (paisB * taxaB)
    ano = ano + 1

    if paisA >= paisB:
        print("A população do País A deve ultrapassar ou igualar a população do País B em %d anos." % ano)