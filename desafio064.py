print('====== DESAFIO 064 ======')
num = soma = cont = 0
num = int(input('Diga um número, para encerrar digite "999": '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Diga um número, para encerrar digite "999": '))
print(f'Você digitou {cont} números, e a soma entre eles foi de {soma}.')
