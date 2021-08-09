real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = float(input('Quanto vale o dólar atual? '))
dolarConv = real/dolar
print('Seu valor convertido em dolares vale {:.2f}' .format(dolarConv))