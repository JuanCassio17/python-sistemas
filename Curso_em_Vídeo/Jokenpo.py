from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('-='*20)
print('VAMOS JOGAR JOKENPO POW?')
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('   KEN')
sleep(1)
print('      PO!!!')
sleep(1)
print('-='*20)
print('O COMPUTADOR ESCOLHEU {}' .format(itens[pc])) #formata com a variavel itens ([])
print('O JOGADOR ESCOLHEU {}' .format(itens[jogador]))
print('-='*20)

if pc == 0: # se computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
     
elif pc == 1: # se o computador jogou papel    
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
        
elif pc == 2: # se o computador jogou tesoura   
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')