"""Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

print("Por favor, informe seu nome e o turno em que você estuda.")

nome = input("Digite seu nome: ").strip()

turno = input("Digite M para Matutino, V para Vespertino ou N para Noturno: ").strip().upper()

if turno == 'M':
    print(f"Bom Dia, {nome}!")
elif turno == 'V':
    print(f"Boa Tarde, {nome}!")
elif turno == 'N':
    print(f"Boa Noite, {nome}!")
else:
    print("Item Inválido!")