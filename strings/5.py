def vertical_invertida():
 nome=input("Digite um nome: ")
 lista = [nome]
 a=1
 b=len(nome)
 for i in lista:
   while a < len(nome):
     if len(i) == b:
       print(i)
       b-=1
     else:
       print(i[:-a])
       a+=1
