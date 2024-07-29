"""Faça um programa que lê três números inteiros e os mostra em ordem
crescente."""

print("Vamos ordenar três números inteiros em ordem crescente.")

while True:
    try:
        
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        numero3 = int(input("Digite o terceiro número: "))

        numeros = [numero1, numero2, numero3]

        numeros.sort()

        print(f"A ordem crescente dos números digitados é: {numeros[0]}, {numeros[1]}, {numeros[2]}")
        break 
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir apenas números inteiros.")