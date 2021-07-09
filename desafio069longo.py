from time import sleep
print('====== DESAFIO 069 ======')
idade = cont = conth = contm20 = 0
sexo = ' '
sn = ' '
confi = ' '
while True:
    print('------ CADASTRO ------')
    idade = int(input('Qual a idade da pessoa? '))
    if idade >= 18:
        cont += 1
    sexo = str(input('Qual o sexo da pessoa? [M/F]: ')).strip().lower()[0]
    if sexo == 'm' and idade < 20:
        contm20 += 1
    if sexo == 'm':
        conth += 1
    if sexo not in 'mf':
        while True:
            sexo = str(input('Qual o sexo da pessoa? [M/F]: ')).strip().lower()[0]
            if sexo == 'm' and idade < 20:
                contm20 += 1
            if sexo == 'm':
                conth += 1
            if sexo in 'f':
                break
            if sexo in 'm':
                break
    while sn not in 'sn':
        sn = str(input('Deseja continar a cadastrar pessoas? [S/N]: ')).strip().lower()[0]
    if sn == 'n':
        break
    if sn not in 's' and 'n':
        while True:
            sn = str(input('Deseja continar a cadastras pessoas? [S/N]: ')).strip().lower()[0]
            if sn == 's' or 'n':
                break
    while confi not in 'sn':
        confi = str(input('Abrir nova ficha? [S/N]: ')).strip().lower()[0]
    if sn in 'Nn' and confi in 'Ss':
        break
    if confi in 'n':
        break
print('-'*10)
print('COMPUTANDO DADOS...')
sleep(2)
print(f'{cont} pessoas tem mais de 18,
foram registrados {conth} homens e {contm20} mulheres tem mais menos de 20 anos.')
print(' ')
print('Obrigado por usar o serviço de registro. Até logo!')
print('-'*10)
