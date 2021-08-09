soma = cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 ==0:
        soma += n
        cont += 1
if cont == 1:
    print(f'Você informou 1 número par e o valor foi {soma}')
else:    
    print(f'Você informou {cont} números pares e a soma foi {soma}')