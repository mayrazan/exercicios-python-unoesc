def vertical():
 nome=input("Digite um nome: ")
 lista = []
 a=0
 while a<=len(nome)-1:
   lista.append(nome[a])
   for i in lista:
     print(i,end='')
   print('\n')
   a+=1
