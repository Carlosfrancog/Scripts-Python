from time import sleep
cor = {"branco":'\033[30m',
       "vermelho":'\033[31m',
       "verde":'\033[32m',
       "amarelo":'\033[33m',
       "azul":'\033[34m',
       "roxo":'\033[35m',
       "ciano":'\033[36m',
       "cinza":'\033[37m',
       "limpa":'\033[m'}
print(f'{cor["ciano"]}====== DESAFIO 029 ======')
v = float(input('Qual a velocidade do carro?'))
m = (v-80)*7
print('PROCESSANDO...')
sleep(1)
if v<80:
    print('Voçê está dentro do limite de velocidade. Tenha um bom dia!')
else:
    print(f'VOÇÊ FOI MULTADO! E TERÁ QUE PAGAR UMA MULTA DE R$ {m:.2f} !')
