num = (int(input('Digite o primeiro número: ')),
int(input('Digite o segundo número: ')),
int(input('Digite terceiro número: ')),
int(input('Digite quarto número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes ') # o comando count conta quantas vezes o número apareceu
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não está em nenhuma posição')    
print('Os valores pares digitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')