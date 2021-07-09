print('====== DESAFIO 090 =====')
aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno(a): ')).strip().upper()
aluno['Média'] = float(input('Digite a média do aluno(a): '))
print('-='*30)
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO(A)'
    print(f"O aluno(a) {aluno['Nome']} está {aluno['Situação']}.")
elif aluno['Média'] >= 5 and aluno['Média'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
    print(f"O aluno(a) {aluno['Nome']} está de {aluno['Situação']}.")
else:
    aluno['Situação'] = 'REPROVADO(A)'
    print(f"O aluno(a) {aluno['Nome']} está {aluno['Situação']}.")
print('-='*30)
for k, v in aluno.items():
    print(f'{k}: {v}')
print('-='*30)
