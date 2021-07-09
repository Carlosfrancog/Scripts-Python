print('====== DESAFIO 084 ======')
pessoas = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('Digite o nome: ')).strip().upper())
    dados.append(float(input('Digite o pesso da pessoa: ').strip()))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    skip = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while skip not in 'SN':
        skip = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if skip in 'N':
        break
print('-='*20)
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai}Kg.', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {men}Kg.', end=' ')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
print()
