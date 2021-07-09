from time import sleep
print('====== DESAFIO 035 ======')
print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
t1 = float(input('PRIMEIRO SEGMENTO:'))
t2 = float(input('SEGUNDO SEGMENTO:'))
t3 = float(input('TERCEIRO SEGMENTO:'))
print('ANALISANDO DADOS...')
sleep(1)
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

#Basta fazer a soma entre os dois lados menores.
# Se a soma entre eles for maior que o terceiro lado, então,
# a soma entre qualquer um deles e o terceiro lado (que é o maior) terá o mesmo resultado.
