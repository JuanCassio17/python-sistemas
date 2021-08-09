print('-='*20)
print('10 TERMOS DE UMA PA')
print('-='*20)

primtermo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))  
décimo = primtermo + (10-1) * razão

for c in range(primtermo, décimo + razão, razão):
    print(f'{c}', end='-> ')
print('ACABOU')