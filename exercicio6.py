"""Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro."""

print("Olá! Bem vindo ao sistema Nanday")

while True:
    login = input("Digite seu login: ")

    senha = input("Digite sua senha: ")

    if login == "admin" and senha == "admin123":
        print("Acesso concedido. Bem-vindo, admin!")
        break 
    else:
        print("Login ou senha incorretos. Tente novamente.")