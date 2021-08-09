from random import randint

computador = randint(1,10)
print('Tente adivinhar meu número')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Digite um numero: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
            print('Mais...')    
    else:
        print('Menos...')
print('O número era {}' .format(computador))
print('Acertasse com {} tentativas' .format(palpites))