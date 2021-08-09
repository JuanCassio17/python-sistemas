nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media >= 4 and media < 7:
    print('Apto a avaliação final')

elif media < 4:
    print('Reprovado')    

else:
    ('Aprovado')    

print(media)