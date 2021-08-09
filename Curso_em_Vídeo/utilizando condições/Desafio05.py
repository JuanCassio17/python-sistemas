from datetime import date
idade = int(input('Digite sua idade: '))
atual = date.today().year
falta = 18 - idade
data = atual - idade
print('Você tem {} anos' .format(idade))


if idade < 18:
    print('Você não pode se alistar')
    print('Falta {} anos' .format(falta))

elif idade == 18:
    print('Você deve se alistar')

else:
    print('Você se alistou em {}' .format(data))