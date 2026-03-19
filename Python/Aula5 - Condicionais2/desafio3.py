age_user = int(input("Digite sua idade: "))
genero = str(input("Digite seu gênero favorito: (ação/drama) ")).lower().strip()

if age_user >14:
    if genero == 'ação':
        print(f'para ao gênero {genero}, recomendamos Batman: O cavalheiro das Trevas')
    elif genero == 'Drama':
        print(f'para ao gênero {genero}, recomendamos O lado bom da vida')
    else:
        print('Gênero não disponível no catálogo ')

else:
    if genero == 'ação':
        print(f'para ao gênero {genero}, recomendamos Os incríveis')
    elif genero == 'drama':
        print(f'para ao gênero {genero}, recomendamos Extraordinário')
    else:
        print('Gênero não disponível no catálogo ')
