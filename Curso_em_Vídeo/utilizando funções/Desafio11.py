from time import sleep
c = ('\033[m', # cor funciona aqui não
'\033[0;30;41m')


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'')
    help(com)
    sleep(2)

def título(msg,cor=0):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0],end='')
    sleep(1)


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP',1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO',1)