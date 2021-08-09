from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR?')
print('-='*20)
jogador = int(input('Digite um número: '))
alternativa = str(input('Par ou Ímpar? [P/I] ')).upper().strip() 
computador = randint(0,10)
total = jogador + computador
print(f'Você jogou {jogador} e o computador jogou {computador}.\nDando um total de {total}.')