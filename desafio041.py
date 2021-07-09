from datetime import date
print('====== DESAFIO 041 ======')
print(' ')
hoje = date.today().year
niver = int(input('Ano de nascimento :'))
idade = hoje - niver
if idade >4 and idade <=9:
    print(f'''O atleta tem {idade} anos.
Classificação: MIRIM''')
elif idade >9 and idade <=14:
    print(f'''O atleta tem {idade} anos.
Classificação: INFANTIL''')
elif idade >14 and idade <=19:
    print(f'''O atleta tem {idade} anos.
Classificação: JÚNIOR''')
elif idade >19 and idade <=25:
    print(f'''O atleta tem {idade} anos.
Classificação: SÊNIOR''')
elif idade >25:
    print(f'''O atleta tem {idade} anos.
Classificação: MASTER''')
elif idade <4:
    print(f'''O atleta tem {idade} anos.
INSCRIÇÃO CANCELADA.
MOTIVO: "muito novo"''')
