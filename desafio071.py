print('====== DESAFIO 071 ======')
print('-'*30)
print('       BANCO COMUNISTA          ')
print('-'*30)
valor = int(input('Quanto quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*60)
print('Volte sempre ao BANCO COMUNISTA! Tenha um bom dia!')
print('='*60)

'''anotações 71

variaveis:
valor = sacar	
total(montnate) recebera o valor
cedula de 50
total de cedulas começa em o x

loop infinito
se o valor  for maior ou igual a 50
o total recebe " - cedula "
a cada retirada de 50 do valor, o total de cedulas recebera +1 x

esse codigo verifica se é possivel retirar e quantas vezes retirar 50 do valor
====================================
se nãó der pra tirar, verifique a cedula atual
 se o valor de cedula for 50, então a proxima celuda vira de 20
e se  não for a de 20, então a cedula se torna de 10
e se não for a de 10, então a cedula se torna de 1
cada vez que muda uma nota ela volta a se tornar 0va
======================================
so vai para quando o total for 0'''

