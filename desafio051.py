print('====== DESAFIO 051 ======')
print('='*25)
print('10 PRIMEIROS TERMOS DA PA')
print('='*25)
termo = int(input('DIGA O 1º TERMO DA PA: '))
razao = int(input('DIGA A RAZÃO DA PA: '))
p10t = termo+(11-1)*razao
print('Os primeiros 10 termos dessa PA são: ')
for c in range(termo, p10t, razao):
    print(f'{c} →',end=' ')
print('ACABOU')
