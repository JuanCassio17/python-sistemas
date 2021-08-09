def dobra(ist):
    pos = 0
    while pos < len(ist):
        ist[pos]*=2
        pos += 1


valores = [1,2,13,13,5]
dobra(valores)
print(valores)