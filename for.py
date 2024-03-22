texto = 'weasdsadasd'
novoTexto = ''
i = 0
tamanho = len(texto)

while i < tamanho:
    print(texto[i])
    i += 1

for letra in texto:
    novoTexto += f'*{letra}'
    print(letra)
    
print(novoTexto + '*')