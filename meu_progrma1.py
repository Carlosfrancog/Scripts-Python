s = float(input('Qual o valor do salário atual? R$'))
por = float(input('Qual a porcentagem adicionada ao salário? %'))
por2 = float(input('Qual a porcentagem retirada do salário? % '))
print(f'O salário de R$ {s:.2f}, com {por}% de aumento ficou em R$ {s+(s*por/100): .2f} .')
print(f'O salário de R$ {s: .2f}, com {por2}% de desconto ficou em R$ {s-(s*por2/100): .2f} .')
