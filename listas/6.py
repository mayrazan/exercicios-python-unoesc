notas = []
alunos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cont = 0
medias = []
n = 0

for a in alunos:
    for i in range(0, 4):
      nota = float(input("Aluno %s - Informe uma nota: " % a))
      if i <= 4:
          cont += nota
    media = cont / 4
    notas.append(media)
    cont = 0
    if media >= 7:
        medias.append(media)
        n += 1

print("O número de alunos com media 7 ou maior é: %d." % n)