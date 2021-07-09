print('==== DESAFIO 023 ==== ')
num = int(input('Digite um número de 0 a 999.999.999.999.999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
M = num // 10000 % 10
b = num // 1000000 % 10
t = num // 10000000 % 10
print(f'Analisando o número {num}, vejo...')
print(f'Unidade:{u}')
print(f'Dezena:{d}')
print(f'Centena:{c}')
print(f'Milhar:{m}')
print(f'Milhão:{M}')
print(f'Bilhão:{b}')
print(f'Trilhão:{t}')
