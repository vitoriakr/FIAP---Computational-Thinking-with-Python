#Coleta de Dados
has_ban = input('Possui um banimento ativo? (sim/não) ').lower().strip()

#Processamento
if has_ban == 'sim':
    rank = 'Bloqueado'
else:
    points = int(input("Digite sua pontuação: "))
    win_rate = float(input('Informe a taxa de vitória (%): '))
    if points > 2500 and win_rate >= 75:
        rank = 'Ouro'
    elif points > 1000 and win_rate >= 50:
        rank ='Prata'
    else:
        rank = 'Bronze'
print(f'Veredito final: {rank}')
