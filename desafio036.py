from time import sleep
cor = {"branco":'\033[30m',
       "vermelho":'\033[31m',
       "verde":'\033[32m',
       "amarelo":'\033[33m',
       "azul":'\033[34m',
       "roxo":'\033[35m',
       "ciano":'\033[36m',
       "cinza":'\033[37m',
       "limpa":'\033[m'}
print('====== DESAFIO 036 ======')
print(' ')
print(f'{cor["roxo"]}Olá, Sou o Robie. sou um robô que vai te ajudar hoje!(/≧▽≦)/ ')
print(f'{cor["azul"]}Me de todas as informações e verei se aprovarei ou não seu emprestímo bancário.{cor["limpa"]}')
print(' ... ')
sleep(1)
casa = float(input(f'{cor["amarelo"]}Qual é o valor da casa em questão? R$'))
salario = float(input(f'Qual é o valor do seu salário mensal? R$'))
anos = float(input(f'Em quantos anos desja parecelar? :'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'As prestações serão de R${prestacao:.2f} anuais{cor["limpa"]}')
print(f'{cor["azul"]}COMPARANDO VALORES...{cor["limpa"]}')
sleep(2)
print(f'Terá que pagar R${prestacao:.2f} e o mínimo é R${minimo:.2f}')
if prestacao <= minimo:
    print(f'{cor["verde"]}SEU EMPRESTIMO FOI APROVADO!{cor["limpa"]}')
else:
    print(f'{cor["vermelho"]}SEU EMPRESTIMO FOI NEGADO!{cor["limpa"]}')
