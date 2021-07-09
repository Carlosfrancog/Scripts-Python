from math import radians,sin,cos,tan
print ( '==== DESAFIO 018 ==== ' )
a = float(input('Digite o ângulo desejado:'))
g = radians(a)
print(f' O ângulo de {a}° tem o SENO de {sin(g):.2f} ')
print(f' O ângulo de {a}° tem o COSSENO de {cos(g):.2f} ')
print(f' O ângulo de {a}° tem a TANGENTE de {tan(g):.2f}')
