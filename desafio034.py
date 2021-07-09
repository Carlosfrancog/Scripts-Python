from time import sleep
print('====== DESAFIO 034 ======')
s = float(input('Qual o valor do salário atual? R$:'))
print('PROCESSANDO DADOS...')
sleep(1)
if s >= 1250:          # a conta feita foi s x 10, dividido por 100 e depois somado s
    print(f'O salário de R$ {s:.2f} recebeu um aumento de 10% e agora é R$ {s+(s*10/100):.2f} .')
else:                 # a conta feita foi s x 15, dividido por 100 e depois somado s
    print(f'O salário de R$ {s:.2f} recebeu um aumento de 15% e agora é R$ {s+(s*15/100):.2f} .')
