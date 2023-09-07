import pandas as pd

# pandas trabalha com Dataframes (tabelas em python)

# ------- Criando um dataframe
#dataframe = pd.DataFrame()

# ------- Criando um dataframe a partir de um dicionário
# 1 crie um dicionário
#venda = {'data': ['15/12/2021', '16/02/2021'],
#         'valor': [500, 300],
#         'produto': ['feijão', 'arroz'],
#        'qtde': [50,70]}

# 2 crie um dataframe e passe o dicionário como parâmetro
#vendas_df = pd.DataFrame(venda)

# ------- Visualizando os dados
#print(vendas_df) # aparece em formato de tabela
# display(vendas_df) -> disponível somente no jupyter

# ------- Importando base de dados
filmes_df = pd.read_excel("filmes.xlsx")
# print(filmes_df)

# ------ Resumos de Visualização de Dados simples e úteis
#print(filmes_df.head())

''' head() mostra as 5 primeiras linhas, 
mas você também pode colocar o número como parâmetro 
para retornar mais valores '''

#print(filmes_df.shape) # quantas linhas e quantas colunas (10,5)

#print(filmes_df.describe()) # mostra a média dos valores numéricos

# ------ Pegar 1 coluna (e os pd.Series)
#filmes = filmes_df['nome'] # recupera apenas o nome dos filmes
#print(filmes) # não retorna um dataframe, é uma série

# um dataframe é uma tabela de séries de dados

# resgatando mais de uma coluna
#filmes = filmes_df[['nome', 'oscar']] # recupera nome e se tem oscar dos filmes
#print(filmes) # é um dataframe, pois retorna mais de uma série

# ------ .loc um método muito importante

# ------ pegar 1 linhas
#print(filmes_df.loc[0])

# ------ pegar dados em um intervalo
#print(filmes_df[0:2])

# ------ pegar linhas de acordo com alguma condição
# print(filmes_df.loc[filmes_df['oscar'] == 'x']) # resgata os filmes que tem oscar. Se tiver x em oscar.

# ------ pegar linhas e colunas específicas
# estrutura do loc ->>>> .loc[linhas, colunas]
# filmes_oscar = filmes_df.loc[filmes_df['oscar'] == 'x', ['nome', 'ano']]
# print(filmes_oscar)

# ------ pegar 1 valor específico
# print(filmes_df.loc[1, 'nome']) # retorna somente o nome de um único valor

# ----- adicionar 1 coluna

# ----- a partir de uma coluna que existe
#filmes_df['bilheteria'] = filmes_df['ano'] * 0.05 # aqui eu dei uma viajada
#print(filmes_df)

# ----- criar uma coluna com valor padrão
# filmes_df['avaliação'] = 0
# print(filmes_df)

# ----- usando loc, mais recomendado
# filmes_df.loc[:,'avaliação'] = 0
# print(filmes_df)
# : significa todas linhas

# ----- adicionar linhas

# ----- importando mais um dataframe
lancamentos2023_df = pd.read_excel('lançamentos2023.xlsx')

# # adicionando os filmes em lançamentos2023 em filmes_df
# filmes_df = pd.concat([filmes_df, lancamentos2023_df])
# print(filmes_df)

# ----- excluindo linhas
# # axis é o eixo da coluna, 0 é o eixo da linha. Bom você sempre definir o eixo
# filmes_df = filmes_df.drop("oscar", axis=1) # excluindo a coluna oscar
# filmes_df = filmes_df.drop(0, axis=0) # excluindo a linha de índice 0
# print(filmes_df)

# ------ valores vazios

# ------ deletar linhas/colunas vazias (tudo)
# filmes_df = filmes_df.dropna(how='all', axis=1)
# print(filmes_df)

# ------ deletar linhas que possuem pelo menos um valor vazio
# filmes_df = filmes_df.dropna() # apaga os filmes que não tem oscar, sem "x" na célula
# print(filmes_df)

# ------ preencher valores vazios (média e último valor)

# ------ preenchendo com um valor padrão
# filmes_df['oscar'] = filmes_df['oscar'].fillna('não') # preenchendo os filmes que não tem oscar com o valor "não"
# print(filmes_df)

# ------ preenchendo com a média da coluna
# nesse dataframe não tem como aplicar esse exemplo, mas o método é .mean()
# filmes_df['oscar'] = filmes_df['oscar'].fillna(filmes_df['oscar'].mean())
# print(filmes_df)

# ------ preenchendo com o último valor
# filmes_df = filmes_df.ffill() 
'''praticamente todos filmes recebem "x" em oscar, 
 menos o primeiro valor.
 Isso acontece porque ele preenche de cima para baixo,
sendo assim, o primeiro valor não tem por onde copiar de cima. '''
# print(filmes_df)

# ------ calcular indicadores

# ------ value counts
# print(filmes_df['ano'].value_counts()) # conta quantos filmes foram lançados por ano

# group by
# filmes_ano = filmes_df[['nome', 'ano']].groupby('ano').count() # agrupa ano e mostra total
# print(filmes_ano)

# ----- mesclar 2 dataframes (procurar informações de um dataframe em outro)
# mais um exemplo que não dá certo com esses dataframes
# filmes_df = filmes_df.merge(lancamentos2023_df)
# print(filmes_df)





