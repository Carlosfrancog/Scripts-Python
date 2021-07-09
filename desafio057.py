print('====== DESAFIO 057 ======')
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # O zero serve para pegar primeira letra
while sexo not in 'MmFf':
    sexo = str(input('DADOS INVALIDOS! Por favor informe seu sexo: ')).strip().upper()[0]
print(f'SEXO {sexo} REGISTRADO COM SUCESSO!')
