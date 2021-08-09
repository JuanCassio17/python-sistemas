from random import randint

usuário = str(input('Digite sua senha: '))
senhas = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
'h', 'i', 'j' ,'k', 'l', 'm', 'n', 'o', 'p', 'q',
'r', 's', 't', 'u', 'w', 'y', 'x','v','z']

passo = ''

while passo != usuário:
    passo = ''
    for letra in range(len(usuário)):
        passo_letra = senhas[randint(0,25)]
        passo = str(passo_letra) + str(passo)
    print(passo)
print(f'Sua senha é {passo}')