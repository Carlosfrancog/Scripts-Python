from random import shuffle
print('==== DESAFIO 020 ==== ')
print('Diga os alunos que estão dispostos a responder na lousa.')
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
list = [a1, a2, a3, a4]
esc = shuffle(list)
print(f'A ordem dos alunos será: {list}')
