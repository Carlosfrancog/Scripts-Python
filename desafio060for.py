print('====== DESAFIO 060 ======')
n = int(input('Digite um número para saber seu fatorial: '))
c = 0
f = 1
for c in range(1,n):
    f *= n
    n -= 1
print(f'Seu fatorial é {f}')
