from random import choice
print('==== DESAFIO 019 ==== ')
print('Diga quais são os alunos dispostos a apagar a lousa. ')
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
list = [a1, a2, a3, a4]               
esc = choice(list)
print(f'O aluno escolhido foi {esc}!')               
