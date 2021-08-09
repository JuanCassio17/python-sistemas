from modularizar import*
from arquivo import*
from time import sleep

arq ='pessoascadastradas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 
    'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de Listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida')
    sleep(2)
