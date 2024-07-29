"""Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.
"""

print("Vamos classificar o seu triângulo com base nos comprimentos dos seus lados.")

def eh_triangulo(lado1, lado2, lado3):
 
  return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

def classificar_triangulo(lado1, lado2, lado3):
 

  if lado1 == lado2 == lado3:
    print("Seu triângulo é equilátero: todos os lados têm o mesmo comprimento.")
  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Seu triângulo é isósceles: dois lados têm o mesmo comprimento.")
  else:
    print("Seu triângulo é escaleno: todos os lados têm comprimentos distintos.")

while True:
  try:
    lado1 = float(input("Informe o comprimento do primeiro lado: "))
    lado2 = float(input("Informe o comprimento do segundo lado: "))
    lado3 = float(input("Informe o comprimento do terceiro lado: "))

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
      print("Os comprimentos dos lados devem ser números positivos.")
    elif not eh_triangulo(lado1, lado2, lado3):
      print("Os valores fornecidos não formam um triângulo. A soma de dois lados deve ser maior que o terceiro lado.")
    else:
      classificar_triangulo(lado1, lado2, lado3)
      break
  except ValueError:
    print("Entrada inválida. Certifique-se de inserir números válidos para os comprimentos dos lados.")