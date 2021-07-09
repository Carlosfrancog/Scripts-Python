from datetime import date
print('====== DESAFIO 054 ======')
hoje = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nascimento= int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    idade = hoje - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'O total de pessoas maiores de idade é: {maior}')
print(f'E o total de pessoas menores de idade é: {menor} ')
