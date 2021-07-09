print('====== DESAFIO 101 ======')


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Você tem {idade} anos, portanto tem o direito ao voto NEGADO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos, portanto tem o direito ao voto OPCIONAL!'
    else:
        return f'Você tem {idade} anos, portanto tem o direito ao voto OBRIGATÓRIO!'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
