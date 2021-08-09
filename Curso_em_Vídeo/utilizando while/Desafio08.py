from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('-=-'*10)
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] OUTROS NÚMEROS
[5] SAIR DO PROGRAMA''')
    print('-=-'*10)
    opção = int(input('>>>>>Qual sua opção? '))
    if opção == 1:
        print('{} + {} = {}' .format(n1,n2, n1+n2))
    elif opção == 2:
        print('{} x {} = {}' .format(n1,n2,n1*n2))
    elif opção == 3:
        if n1 > n2:
            print('{} é maior que {}' .format(n1, n2))
        else:
            print('{} é maior que {}' .format(n2,n1))    
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')        
    sleep(2)
print('Volte sempre!')