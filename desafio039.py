print('====== DESAFIO 039 ======')
print(' ')
sexo = int(input('''Informe o seu sexo: 
[ 1 ] Masculino
[ 2 ] Feminino
Opção: '''))
from datetime import date

if sexo == 1:
    nasc = int(input('Informe o ano do seu nascimento:'))
    hoje = date.today().year
    resta = 18 - (hoje - nasc)
    passou = (hoje - nasc) - 18
    idade = hoje - nasc

    print(f'Quem nasceu em {nasc} tem {idade} anos em {hoje}.')
    if idade > 18:
        print(f'Você já deveria ter se alistado ha {passou} anos.')
        print(f'Seu alistamento foi em {nasc+18}')
    elif idade < 18:
        print(f'Você irá se alistar daqui há {resta} anos.')
        print(f'Seu alistamento será em {nasc+18}.')
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
elif sexo == 2:
    print('Você não precisa se alistar.')
