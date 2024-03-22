nome = 'luis'
numero = 123123.2234324

variavel = '%s, o preco é %.2f' % (nome, numero)
print(variavel)

letra = 'abc'

print(f'{letra}')
print(f'{letra: >10}')
print(f'{letra: <10}.')
print(f'{letra: ^10}.')

print(f'{1000.123123523352: .1f}')
print(f'{1500: 08x}')

print(nome[0:2])

mundo = 'ola mundo'
print(len(mundo))
print(mundo[0:9:3])