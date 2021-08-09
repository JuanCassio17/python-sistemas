def mostra_linha():
    print('-=~'*20)


cin = 0.05
dez = 0.10
vincin = 0.25
cinqu = 0.50 
real = 1.00 
mostra_linha()
print('---------------------CÁLCULO DE MOEDAS---------------------')
mostra_linha()
valor1 = int(input('Quantas moedas de 0.05c? '))
valor2 = int(input('Quantas moedas de 0.10c? '))
valor3 = int(input('Quantas moedas de 0.25c? '))
valor4 = int(input('Quantas moedas de 0.50c? '))
valor5 = int(input('Quantas moedas de R$1.00? '))
total = (valor1*cin) + (valor2*dez) + (valor3*vincin) + (valor4*cinqu) + (valor5*real)
print(f'Você tem ao todo R${total:.2f}')

if total < 10:
    print(f'Falta R${10-total:.2f} para completar R$10.00 reais')
else:
    print('Você já pode trocar suas moedas em uma nota de R$10.00 reais')
