estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Digite o Estado: '))
    estado['sigla'] = str(input('Digite a sigla do Estado: '))
    brasil.append(estado.copy()) #.copy - faz a cópia
for e in brasil:
    for v in e.values():
        print(v)