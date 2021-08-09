contapessoas = 0
conta18 = 0
contamulheres = 0
while True:
    print('='*20)
    print('CADASTRE UMA PESSOA')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()
    print('='*20)
    parar = str(input('Deseja parar? [S/N] ')).upper().strip()
    if parar == 'S':
        break
    elif idade >= 18:
        conta18 += 1
    elif contapessoas == True:
        contapessoa += 1
    elif idade > 21 and sexo == 'F' == True:
        contamulheres += 1


print('Tudo bem, até mais!')
print(f'Há {conta18} pessoas com 18 anos')        
print(f'Há {contapessoas} cadastrados')
print(f'Há {contamulheres} mulheres com menos de 21 anos cadastradas')