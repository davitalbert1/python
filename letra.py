frase = 'edrefdfwsdsfwefedsdfsfdd'
mais = 0
letraVezes = ''

print(frase.count('d'))

i=0

while i < len(frase):
    letraAtual = frase[i]
    vezes = frase.count(letraAtual)
    
    if mais < vezes:
        mais = vezes
        letraVezes = letraAtual
    
    print(letraAtual, vezes)
    i += 1
    
print(mais)
print(letraVezes)