valor = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa''')

usuario = int(input('Digite sua interação: '))

if usuario == 1:
    print(valor+valor2)

elif usuario == 2:
    print(valor*valor2)    

elif usuario == 3:
    if valor > valor2:
        print('{}' .format(valor))
    else:
        print('{}' .format(valor2))    

elif usuario == 4:
    print('Não sei o que seja novos numeros')

elif usuario == 5:
    print('ok até mais')