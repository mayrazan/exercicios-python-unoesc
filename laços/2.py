usuario = input("Informe um usuario: ")
senha = input("Informe uma senha: ")

while usuario == senha:
    print("Erro. Usuario e senha não podem ser iguais, tente novamente.")
    
    usuario = input("Informe um usuario: ")
    senha = input("Informe uma senha: ")

print("Usuario e senha ok.")