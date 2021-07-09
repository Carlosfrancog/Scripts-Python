from time import sleep
print('====== DESAFIO 042 ======')
print('-=-'*20)
print('Analisador de triângulos v2.0')
print('-=-'*20)
t1 = float(input('PRIMEIRO SEGMENTO:'))
t2 = float(input('SEGUNDO SEGMENTO:'))
t3 = float(input('TERCEIRO SEGMENTO:'))
print('ANALISANDO DADOS...')
sleep(1)
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if t1 == t2 == t3:
      print('EQUILÁTERO!')
    elif t1 != t2 != t3 != t1:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo !')
    
