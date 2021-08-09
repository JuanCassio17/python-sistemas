from random import randint
from time import sleep #esse modulo faz o programa ter um time de processamento
n = randint(1,5)
adivinha = int(input('Qual número? '))
print('Processando...')
sleep(2) #esse comando espera por 2 segundos a resposta do programa
if n == adivinha:
    print('Você acertou')
else:
    print('Tente mais uma vez') 
print('O número era {}' .format(n))