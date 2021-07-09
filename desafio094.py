print('====== DESAFIO 094 ======')
dados = dict()
galera = list()
numcad = soma = media = 0
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: ')).strip().upper()
    dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dados['Idade'] = int(input('Idade: '))
    numcad += 1
    soma += dados['Idade']
    galera.append(dados.copy())
    skip = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while skip not in 'SN':
        skip = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if skip in 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {numcad} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ',end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f"{p['Nome']}, ", end='')
print()
print('D) Lista de pessoa que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
