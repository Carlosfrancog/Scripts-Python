print('====== DESAFIO 070 ======')
num = soma = prod1000 = menor = cont = 0
nomes = ' '
nomeprod = ' '
while True:
    print('-='*10)
    nomes = str(input('Nome do produto: ')).strip().upper()
    num = float(input('Valor do produto R$: '))
    if num > 1000:
        prod1000 += 1
    if cont == 1:
        menor = num
    else:
        if num < menor:
            menor == num
    if cont == 1 or num < menor:
        menor = num
        nomeprod = nomes
    soma += num
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
print('-='*13)
print(f'O valor total da compra é de R${soma:.2f}')
print(f'O total de produtos que ultrapassam R$1000.00 é de: {prod1000}')
print(f'O produto mais barato custa R${num:.2f} . E o produto foi "{nomes}".')
print('-='*13)
