s = 0
c = 0
print('Somando os multiplos de 3.')
i = int(input('Valor do inicio do range: '))
f = int(input('Valor do final do range: '))
for m in range(i, f):
    if m % 3 == 0:
        print(f'{m}', end='\n')
        c += 1
        s += m
print(f'total da soma dos numeros {s}, e os numeros encontrados no range {c}')
