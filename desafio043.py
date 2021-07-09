print('====== DESAFIO 043 ======')
print(' ')
peso = float(input('DIGA SEU PESO EM KG:'))
altura = float(input('DIGA SUA ALTURA EM METROS:'))
imc = peso/(altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('PESO IDEAL!')
elif 25 <= imc < 30:
    print('SOBREPESO!')
elif 30 <= imc < 40:
    print('OBESIDADE!')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA!')
