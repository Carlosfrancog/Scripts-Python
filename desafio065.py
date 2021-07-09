print('===== DESAFIO 065 =====')
num = media = maior = menor = soma = qunat = 0
p = 's'
while p in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qunat += 1
    if qunat == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    p = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
media = soma/qunat
print(f'Você dogotou {qunat} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
