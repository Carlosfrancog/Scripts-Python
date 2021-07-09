print('====== DESAFIO 078 ======')
valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-='*30)
print(f'Os valores da lista são: {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f' {i}...', end='')
print()
print(f'O menor valor digitado foi {min(valores)} nas posições', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f' {i}...', end='')
print()
