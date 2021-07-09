from time import sleep
print('====== DESAFIO 040 ======')
print(' ')
n1 = float(input('Primeira nota do aluno :'))
n2 = float(input('Segunda nota do aluno :'))
media = (n1+n2)/2
print('CALCULANDO...')
sleep(1.5)
print(f'Tirando {n1:.1f} e {n2:.1f} a média é {media:.1f}')
print('COMPILANDO...')
sleep(1.5)
if media <=5.0:
    print(f'A média do aluno foi {media:.1f}. Como está abaixo de 5, o aluno está REPROVADO!')
elif media >=5.0 and media < 7.0:
    print(f'A média do aluno foi {media:.1f}. Como está entre 5 e 7, o aluno está de RECUPERAÇÃO!')
elif media > 7.0:
    print(f'A média desse aluno foi {media:.1f}. Como está acima de 7, o aluno está APROVADO!')

        
