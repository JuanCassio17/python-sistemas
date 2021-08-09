km = float(input('Qual a km que o carro andou? '))
multa = (km-80) * 7

if km > 80:
    print('Você foi multado')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa)) 
else:
    print('Siga bem e boa viagem')