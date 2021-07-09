print('====== DESAFIO 049 ======')
print('-=-'*10)
n = int(input('Digite um número para ver sua taboada: '))
print('-=-'*10)
for c in range(1, 11):
    print(f'{n:2}  x {c:2} = {n*c}')
