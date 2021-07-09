print('====== DESAFIO 026 ======')
frase = str(input('Digite uma frase:')).lower().strip()
l = frase.count('a')
f = frase.find('a')+1
u = frase.rfind('a')+1
print(f'A letra "A" aparece {l} vezes na farse "{frase}". ')
print(f'A primeira letra "A" apareceu na posição {f} da frase.')
print(f'A última letra "A" apareceu na posição {u} da frase.')
