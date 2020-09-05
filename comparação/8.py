produto1 = float(input("Qual o valor do produto 1 em R$? "))
produto2 = float(input("Qual o valor do produto 2 em R$? "))
produto3 = float(input("Qual o valor do produto 3 em R$? "))

if produto1 < produto2 and produto1 < produto3:
    print("Você deve comprar o produto 1")
elif produto2 < produto1 and produto2 < produto3:
  	print("Você deve comprar o produto 2")
elif produto3 < produto1 and produto3 < produto2:
    print("Você deve comprar o produto 3")