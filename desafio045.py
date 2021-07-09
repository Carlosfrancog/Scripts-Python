from random import randint
from time import sleep
lista = ("Pedra", "papel", "Tesoura")
computador = randint(0, 2)
pergutar = int(input('''ESCOLHA UMA OPÇÃO:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
DIGITE SUA ESCOLHA:'''))
if pergutar > 2:
    print('OPÇÃO INVALIDA!')
else:
    print('JO')
    sleep(0.50)
    print('KEN')
    sleep(0.50)
    print('POOH !')
    print('-=-'*10)
    print(f'O Computador escolheu: {lista[computador]}')
    print(f'O Jogador escolheu: {lista[pergutar]}')
    print('-=-'*10)
if computador == 0:
    if pergutar == 0:
        print('EMPATE !')
    elif pergutar == 1:
        print('JOGADOR VENCEU!')
    elif pergutar == 2:
        print('COMPUTADOR VECEU !')
if computador == 1:
    if pergutar == 0:
        print('COMPUTADOR VENCEU !')
    elif pergutar == 1:
        print('EMPATE !')
    elif pergutar == 2:
        print('JOGADOR VENCEU !')
if computador == 2:
    if pergutar == 0:
        print('JOGADOR VENCEU !')
    elif pergutar == 1:
        print('COMPUTADOR VENCEU !')
    elif pergutar == 2:
        print('EMPATE !')
print('-=-'*10)
print('OBRIGADO POR JOGAR !')
