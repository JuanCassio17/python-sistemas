números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor já inserido. Insira outro')        
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*20)
números.sort()
print(f'Você digitou os números {números}')