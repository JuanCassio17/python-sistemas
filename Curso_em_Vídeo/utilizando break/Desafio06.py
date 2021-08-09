while True:
    n = int(input('Digite um número: '))    
    if n < 0:
        break
    print('-'*30)
    for c in range(1,11): # pode utilizar o for in range
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO')