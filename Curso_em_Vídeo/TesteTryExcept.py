#UTILIZANDO O TRY E O EXCEPT
'''testa se de fato o usuário escreveu dois valores, caso o contrário
ele apresenta uma mensagem super educada. 
Se o usuário for inteligente, ele realiza a conta '''

try:
    valor1 = float(input('Digite um valor:'))
    valor2 = float(input('Digite o segundo valor:'))

except:
    print('você é burro? deve-se inserir números decimais apenas')

else:
    print(valor1+valor2)    