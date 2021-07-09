print('====== DESAFIO 082 ======')
listapar = list()
listaimpar = list()
lista = list()
while True:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        listapar.append(num)
        lista.append(num)
    elif num % 2 == 1:
        listaimpar.append(num)
        lista.append(num)
    skip = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while skip not in 'SN':
        skip = str(input('Invalido! Quer continuar? [S/N]: ')).strip().upper()[0]
    if skip in 'N':
        break
listapar.sort()
listaimpar.sort()
lista.sort()
print('-='*30)
print(f'A lista geral de números adicionados foi: {lista}')
print(f'Na lista de números pares foram adicionados os números: {listapar}')
print(f'Na lista de números impares foram adicionados os números: {listaimpar}')
