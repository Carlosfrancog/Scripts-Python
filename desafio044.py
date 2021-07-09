print('====== DESAFIO 044 ======')
print(' ')
prod = float(input('Qual o valor da compra? R$:'))   # "prod" é o valor da compra.
avista = prod*(10/100)                               # "avista" é o calculo da opção 1.
avcard = prod*(5/100)                                # "avcard" é o calculo da opção 2.
x2card = prod                                        # "x2card" é o calculo da opção 3.
x3maiscard = prod+(prod*(20/100))                    # "x3maiscard" é o calculo da opção 4.
escolha = int(input('''Escolha uma forma de pagamento.
[1] À vista no dinheiro ou cheque (-10%).
[2] À vista no cartão (-5%).
[3] Em 2x no cartão (SEM JUROS).
[4] Em 3x ou mais no cartão (+20% de juros).
ESCOLHA:'''))
if escolha == 1:
    print(f'A compra de R${prod:.2f} a vista no dinheiro/cheque ficou em R${prod-(avista):.2f} .')
elif escolha == 2:
    print(f'A compra de R${prod:.2f} a vista no cartão ficou em R${prod-(avcard):.2f} .')
elif escolha == 3:
    print(f'A compra de R${prod:.2f} será pareclada em 2x de {prod/2:.2f}.')
elif escolha == 4:
    parcelas1 = int(input('Quantas parcelas serão? :'))  # "parcelas1" pergunta a quantidade de parcelas.
    total = x3maiscard/parcelas1 # "total" é o calculo das parcelas.
    print(f'''Sua compra de R${prod:.2f} será parcelada em {parcelas1}x de R${total:.2f}. (COM JUROS).
Sua compra de R${prod:.2f} vai acabar custando R${x3maiscard:.2f} no final.''')
else:
    print('OPÇÃO INVALIDA! TENTE NOVAMENTE.')
