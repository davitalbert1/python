numero = 10

linha = 1
coluna = 1

qtLinha = numero
qtColuna = numero

while linha <= qtLinha:
    coluna = 1
    while coluna <= qtColuna:
        print(f'{linha} {coluna}')
        coluna += 1
    linha += 1