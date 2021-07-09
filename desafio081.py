print('====== DESAFIO 081 ======')
lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    skip = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while skip not in 'SN':
        skip = str(input('Tente novamente. Quer continuar? [S/N]: ')).strip().upper()[0]
    if skip in 'N':
        break
print(f'Sua lista é: {lista}')
print(f'Você adicionou {len(lista)} valores a lista.')
lista.sort(reverse=True)
print(f'Essa lista com os valores organizados por ordem de crescimento é: {lista}')
if 5 not in lista:
    print('O valor 5 não foi adicionado na lista!')
else:
    print(f'O valor 5 foi adicionado na lista, e está na posição {lista.index(5)+1} ')
