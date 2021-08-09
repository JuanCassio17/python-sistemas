from random import randint
v = 0

print('='*30)
print('VAMOS JOGAR PAR OU IMPAR')
print('='*30)

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    opção = ' ' 
    while opção not in 'PI':
        opção = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    if opção == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu')    
            break
    elif opção == 'I':
        if total % 2 == 1:
            print('Você venceu')        
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente.........')    
print(f'Você venceu {v} vezes')