print('='*20)
print('   SUPER BARATÃO')
print('='*20)
total = 0
produtos = 0

while True:
    nomepro = str(input('Nome do produto: ')).upper()
    preço = float(input('Qual foi o preço? R$ '))
    parar = str(input('Quer continuar? [S/N] ')).upper().strip()
    total += preço
    if parar == 'N':
        break
print('Tudo bem! até mais')  
print(f'Você gastou R${total:.2f}')