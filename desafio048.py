print('====== DESAFIO 48 ======')
s = 0
c = 0
c2 = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n
        c += 1
    c2 += 1
print(f'''Entre 1 e 500, existem {c2} números ímpares,
os valores divisiveis por 3 são {c}
e a soma desses valores resulta em {s}''')
