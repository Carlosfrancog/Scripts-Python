print('====== DESAFIO 096 ======')


def area(x, y):
    print('-'*40)
    print(f'''A largura é {x}m e o comprimento é {y}m
portanto a área desse terreno é de {x*y} m²''')



area(float(input('Digite a largura em metros: ')), float(input('Digite o comprimento em metros: ')))
