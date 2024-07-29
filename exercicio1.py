##Faça um Programa que peça dois números e imprima o maior deles.

print("Digite dois números e descubra qual é o maior.")

numero1 = float(input("Digite o primeiro número: "))

numero2 = float(input("Digite o segundo número: "))


if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Os números são iguais.")