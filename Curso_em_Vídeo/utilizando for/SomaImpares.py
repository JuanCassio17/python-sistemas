# QUESTÃO SOMA IMPARES MULTIPLOS DE TRES
soma = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos valores solicidatos é {soma}. Tendo {cont} termos.')