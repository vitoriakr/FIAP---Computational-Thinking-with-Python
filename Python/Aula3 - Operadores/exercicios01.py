#Faça um programa que leia receba a entrada de um num inteiro e mostre em tela o seu sucessor e antecessor
num3 = int(input("Digite um numero: "))
print(f"o antecessor do numero {num3} é {num3 - 1} e p sucessor do numero {num3 + 1}")

# ex 2: Escreva um programa que pergunte a qtd de km percorridos por um carro ..
km_percorrido = float(input("Digite quantos km foram percorridos: "))
dias_alugados = int(input("Digite quantos diar foram alugados: "))
valor_km = km_percorrido * 0.20
valor_dia = dias_alugados * 80
print(f' o valor a ser pago é {valor_km + valor_dia}')
