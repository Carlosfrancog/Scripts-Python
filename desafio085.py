print('====== DESAFIO 085 ======')
numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o valor para a {c}º posição: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-='*10)
print(f'Os números pares digitados foram: {sorted(numeros[0])}')
print(f'Os números ímpares digitados foram: {sorted(numeros[1])}')
