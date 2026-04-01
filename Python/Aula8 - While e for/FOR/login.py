#login no sistema
target_user = "admin_sistema"
max_attempts = 3
is_authenticated = False
print('AUTENTICAÇÃO NO SISTEMA')

for attempt in range(1, max_attempts + 1):
    print(f'\nTentativa {attempt} de {max_attempts}')
    input_user = input('Digite o nome de usuário: ')
    if input_user == target_user:
        is_authenticated = True
        print('Usuário autenticado com sucesso!')
        break
    else:
        print('Nome de usuário incorreto.')

if not is_authenticated:
    print('Número máximo de tentativas excedido. Acesso negado.')