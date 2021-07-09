print('====== DESAFIO 079 ======')
valores = list()
while True:
    num = int(input('Digite qualquer valor: '))
    if num in valores:
        print('Valor já adicionado! Digite outro.')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'N':
            break
        while resp not in 'SN':
            resp = str(input('Tente novamente. Quer continuar? [S/N]: ')).strip().upper()[0]
            if resp in 'N':
                break
    else:
        valores.append(num)
        print('Valor adicionado!')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'N':
            break
        while resp not in 'SN':
            resp = str(input('Tente novamente. Quer continuar? [S/N]: ')).strip().upper()[0]
            if resp in 'N':
                break
print('='*30)
valores.sort()
print(f'Os valores organizados por ordem de crescimento ficou: {valores}')
