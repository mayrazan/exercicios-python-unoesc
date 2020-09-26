def imprime(numero):
 i = 1
 lista = []
 while i <= numero:
   lista.append(i)
   for e in lista:
     print(e, end = ' ')
   print('\n')
   i+=1
