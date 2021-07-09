from random import randint
print('====== DESAFIO 058 ======')
# L = está dentro do laço, NL = não está dentrp do laço
nuntentativas = 0  # números de tentativas    NL
pc = randint(0, 10)  # randomiza um número de 0 a 10    NL
print('Vou pensar em um número de 0 a 10 tente adivinhar. ')  # msg do pc   NL
vc = int(input('Diga seu palpite: '))  # primeiro palpite   NL
while vc != pc:  # em quanto 'vc' for diferente de 'pc' esse laço se repitirá  *inicio do laço*
    if vc <= 10:  # se 'vc' for menor ou = a 10...   L
        if vc < pc:  # se 'vc' for menor que 'pc'    L
            print('ERROU... dica: tente um número maior')  # tentar novamente num maior   L
        elif vc > pc:  # se 'vc' for maior que 'pc'    L
            print('ERROU... dica: tente um número menor')  # tentar novamente num menor   L
        vc = int(input('Diga seu palpite: '))  # palpite no laço de repetição até acertar   L
        nuntentativas += 1  # adiciona +1 a cada tentativa feita   L
    elif vc > 10:  # se o palpite for maior que 10...     L
        print('PALPITE INVÁLIDO. Tente novamente. ')  # msg de invalidez   L
        vc = int(input('Diga seu palpite: '))  # tentar novamente   L  *fim do laço*
if nuntentativas == 1:  # se acertar na primeira tentativa  "
    print('MUITO BEM! Você acertou, e precisou de uma tentativa.')  # msg de uma tentativa  NL
elif nuntentativas != 1:  # se o num de tentativas for diferente de 1
    print(f'MUITO BEM ! Você acertou, e precisou de {nuntentativas +1} tentativas.')
    # msg de + de uma tentativa para acertar 
