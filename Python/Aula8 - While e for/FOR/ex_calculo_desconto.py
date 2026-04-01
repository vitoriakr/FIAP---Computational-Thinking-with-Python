#calculo de desconto
num_products = 4
discount = 0.15
for i in range(1, num_products + 1):
    price = float(input(f'Digite o preço do produto {i}: '))
    if price > 100:
        final_price = price * (1 - discount)
        print(f'O preço final do produto {i} com desconto é: R${final_price:.2f}')
    else:
        print(f'O preço do produto {i} é: R${price:.2f} (sem desconto)')
    
    