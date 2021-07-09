print('====== DESAFIO 075 ======')
nuns = (int(input('Digite um número: ')), int(input('Digite outo número: ')),
        int(input('Digite mais um número: ')),int(input('Digite um útimo número: ')))
print(f'Os números digitados foram: {nuns}')
print(f'O número 9 apareceu {nuns.count(9)} vezes.')
if 3 in nuns:
    print(f'O primeiro número 3 está na {nuns.index(3)+1}º posição')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ',end='')
for n in nuns:
    if n % 2 == 0:
        print(n, end=' ')

