from time import sleep
print('====== DESAFIO 059 ======')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('=-='*10)
    sleep(1)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opçao = int(input('>>>>>Qual é a sua opção? '))
    if opçao == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
    elif opçao == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
    elif opçao == 3:
        print(f'Entre {n1} e {n2} o maior é {max(n1,n2)}')
    elif opçao == 4:
       print('Informe os numeros novamente:')
       n1 = int(input('Primeiro valor: '))
       n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('FINALIZANDO...')
        sleep(1)
    else:
        print('Opção invalida. Tnte novamente.')
print('Fim do programa! Volte sempre!')
