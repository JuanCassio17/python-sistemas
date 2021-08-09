n = s = 0           
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
#print('A soma vale {}' .format(s))    
print(f'A soma vale {s}.\nTeve {cont} números somados.'),
#print(f'Teve {cont} de números somados')