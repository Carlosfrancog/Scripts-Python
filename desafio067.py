print('====== DESAFIO 067 ======')
n = 0
print('-=-' * 17)
while True:
    n = int(input('Digite um número para ver sua taboada: '))
    print('-=-' * 17)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n:2}  x {c:2} = {n * c}')
    print('-=-' * 17)
print('GERADOR DE TABOADA ENCERRADO. Volte sempre!')
print('-=-'*17)
