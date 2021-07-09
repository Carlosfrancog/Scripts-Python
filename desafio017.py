from math import hypot
print ( '==== DESAFIO 017 ==== ' )
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
