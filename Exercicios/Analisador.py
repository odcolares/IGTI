mi = 0
hv = 0
print('analisando informações!')
for info in range(0, 2):
    nome = str(input('digite o nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite qual o seu sexo M ou F: ')).capitalize()
    mi += idade / 2
    if sexo in 'M m':
        print()
print(f'{mi:.0f} anos de idade.')

