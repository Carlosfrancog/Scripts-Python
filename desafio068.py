from random import randint
print('====== DESAFIO 068 ======')
vc = c = s = 0
pi = ''
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    numpc = randint(1, 10)
    vc = int(input('Digite um número: '))
    pi = str(input('Par ou Ímpar? [P/I]: ')).strip().lower()[0]
    s = (vc + numpc)
    par = (vc + numpc) % 2 == 0
    impar = (vc + numpc) % 2 != 0
    if impar:
        print(f'O jogador jogou {vc} e o computador jogou {numpc}. Tendo ressultado {s} é ÍMPAR!')
    if par:
        print(f'O jogador jogou {vc} e o computador jogou {numpc}. Tendo ressultado {s} é PAR!')
    print('=-'*15)
    if par and pi in 'Pp':
        print('GANHOU! Vamos jogar de novo.')
        c += 1
    elif impar and pi in 'Ii':
        print('GANHOU! Vamos jogar de novo.')
        c += 1
    else:
        print('PERDEU!')
        break
print(f'Você perdeu! Seu total de vitórias acumuladas é de {c} vitórias.')
