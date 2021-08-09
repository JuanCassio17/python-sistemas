from time import sleep #usando módulo para o intervalo do laço
from statistics import harmonic_mean #usando módulo para calcular a média harmônica
while True:
    print('---CALCULANDO MÉDIAS---')
    print('-='*20)
    print('ESCOLHA O QUE DESEJA CALCULAR:')
    print("""[A] MÉDIA ARITMÉTICA
[P] MÉDIA PONDERADA
[H] MÉDIA HARMÔNICA""")
    print('-='*20)
    print('-='*20)
    
    EscolhaUsu = str(input('Digite sua opção: [A/P/H] ')).strip().upper()[0]
    
    while EscolhaUsu not in 'APHS':
        EscolhaUsu = str(input('Digite sua opção: [A/P/H] ')).strip().upper()[0]
    
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    valor3 = float(input('Digite o terceiro valor: '))

    print('-='*20)
    
    if EscolhaUsu == 'A':
        print(f'A Média Aritmética dos valores é {(valor1+valor2+valor3)/3:.2f}')
        sleep(2)
        print('-='*20)
        print('[0] SAIR\n[1] CONINUAR')
        parar = int(input('Deseja sair do programa? [0/1] '))
        if parar == 0:
            break
        else:
            continue

    elif EscolhaUsu == 'P':
        print(f'A Média Ponderada dos valores é {(valor1*5 + valor2*3 + valor3*2)/10:.2f}')
        sleep(2)
        print('-='*20)
        print('[0] SAIR\n[1] CONINUAR')
        parar = int(input('Deseja sair do programa? [0/1] '))
        if parar == 0:
            break
        else:
            continue
    
    elif EscolhaUsu == 'H':
        print(f'A Média Harmônica dos valores é {harmonic_mean([valor1,valor2,valor3]):.2f}') #o módulo vai simplificar a fração
        sleep(2)
        print('-='*20)
        print('[0] SAIR\n[1] CONINUAR')
        parar = int(input('Deseja sair do programa? [0/1] '))
        if parar == 0:
            break
        else:
            continue

print('VOCÊ SAIU DO PROGRAMA!')       
sleep(2)
print('Até a próxima!')