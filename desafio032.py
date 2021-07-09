while(True)
from calendar import isleap
from datetime import date
from time import sleep
print('====== DESAFIO 032 ======')
Year = int(input('Digite o ano para saber se ele é bissexto ou não.\n Para verificar o ano atual pode-se digitar 0 .'))
print('VERIFICANDO...')
sleep(1)
if Year == 0:
    Year = date.today().year
if isleap(Year) == True:
    print(f'O ano {Year} é BISSEXTO.')
else:
    print(f'O ano {Year} NÃO É BISSEXTO.')
# "Year" com o y em maíusculo é o objeto, e year com o y mínusculo é refrente aos modulos.
