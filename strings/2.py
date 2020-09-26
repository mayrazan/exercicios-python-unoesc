
def reverso():
 nome = input("Digite um nome: ")
 if(nome.islower()):
   print(nome.upper()[::-1])
 elif(nome.isupper()):
   print(nome.lower()[::-1])
