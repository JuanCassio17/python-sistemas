nomes = ('Atletico', 'Internacional', 'SPaulo', 'Palmeiras', 'Vasco',
'Flamengo', 'Fluminense', 'Sport', 'Santos', 'Fortaleza')
for p in nomes:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')