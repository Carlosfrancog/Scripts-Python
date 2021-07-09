print('====== DESAFIO 053 ======')
frase = str(input('DIGITE UMA FRASE: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inv = ''
inv= junto[::-1] #sem o for
'''for letra in range(len(junto)-1,-1,-1): #com o for
    inv += junto[letra]'''
print(f'O inverso de {junto} é {inv}')
if inv == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
