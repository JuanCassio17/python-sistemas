from time import sleep
print('-='*20)
print('Vou analisar seus números:')

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if a > b:
    print('Processando...')
    sleep(2)
    print('Número {} é maior que {}' .format(a,b))

elif a < b:
    print('Processando...')
    sleep(2)
    print('Número {} é menor que {}' .format(a,b))    

else:
    print('Processando...')
    sleep(2)
    print('Números iguais')  

print('-='*20)