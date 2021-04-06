print('Descobrir qnts numeros pares a no range escolhido! ')
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
for p in range(v1, v2 + 1):
    if p % 2 == 0:
        print(p, end=' ')
print('Fim')
