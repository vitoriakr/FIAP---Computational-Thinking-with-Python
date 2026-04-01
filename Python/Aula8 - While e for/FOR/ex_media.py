#Calcular a média de 4 notas de um aluno
some_notas = 0
total_de_provas = 4
for i in range(1,5):
    nota = float(input(f'Digite a {i} nota da prova do aluno: '))
    some_notas += nota #ou soma_notas = some_notas + nota
    media = some_notas / total_de_provas
print(f'A média do aluno é: {media}')


