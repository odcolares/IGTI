inicio = int(input('Inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))

for c in range(inicio, fim+1, passo):
    print(c)
print('Acabou!')