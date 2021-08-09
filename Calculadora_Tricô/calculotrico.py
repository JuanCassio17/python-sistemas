def mostra_linha():
    print('-=~'*20)


mostra_linha()
print('-----------------CÁLCULO DE PONTOS EM TRICÔ-----------------')
mostra_linha()
lar = float(input('Qual largura? '))
alt = float(input('Qual altura? '))
apontos = float(input('Quantos cm tem sua amostra em pontos? '))
acarreiras = float(input('Quantos cm tem sua amostra em carreiras? '))
pontos = lar*10//apontos
carreiras = alt*10//acarreiras
print('Você vai precisar de {} pontos' .format(pontos))
print('Você vai precisar de {} carreiras' .format(carreiras))
