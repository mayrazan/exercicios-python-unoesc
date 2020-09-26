def tamanho():
 cont1=0
 cont2=0
 palavra = input("Digite uma palavra: ")
 palavra2 = input("Digite uma palavra: ")
 print("String1: " + palavra)
 print("String2: " + palavra2)
 cont1 = len(palavra)
 cont2 = len(palavra2)
 print("Tamanho de " + palavra + ": " + str(cont1) + " caracteres")
 print("Tamanho de " + palavra2 + ": " + str(cont2) + " caracteres")
 if(cont1==cont2):
   print("As duas strings possuem o mesmo tamanho")
 else:
   print("As duas strings são de tamanhos diferentes")
 if(palavra!=palavra2):
   print("As duas strings possuem conteúdo diferente")
 else:
   print("As duas strings possuem o mesmo conteúdo")
