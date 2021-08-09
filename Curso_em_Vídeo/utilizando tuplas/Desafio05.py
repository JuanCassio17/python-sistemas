lista = ('Arroz', 2.50,
'Cuscuz', 5.50, 
'Margarina', 10.15, 
'Mandioca', 35.18)
print('-='*20)
print(f'{"LISTAGEM DE COMPRAS":^40}')        
print('-='*20)
for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end= '')
    else:
        print(f'R${lista[pos]:.<7.2f}')    
print('-='*20)