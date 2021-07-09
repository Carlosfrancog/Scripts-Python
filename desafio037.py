cor = {"AZUL":'\033[34m',
       "VERDE":'\033[31m',
       "CIANO":'\033[36m',
       "limpa":'\033[m'}
print('====== DESAFIO 037 ======')
print(' ')
n = int(input('Digite um número inteiro:'))
print(f'''Escolha uma das bases para conversão:
{cor["AZUL"]}[1] converter para BINARIO{cor["limpa"]}
{cor["VERDE"]}[2] converter para OCTAL{cor["limpa"]}
{cor["CIANO"]}[3] converter para HEXADECIMAL{cor["limpa"]}''')
opç = int(input('Sua opção:'))
if opç == 1:
    print(f'{n} em BINARIO é: {bin(n)[2:]}')
elif opç == 2:
    print(f'{n} em OCTAL é: {oct(n)[2:]}')
elif opç == 3:
    print(f'{n} em HEXADECIMAL é: {hex(n)[2:]}')
else:
    print('OPÇÃO INVALIDA!')
