n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
r1 = n1 / n2
r2 = n1 * n2

print('Qual operação matematica vc deseja escolher: Multiplicação ou Divisão?\n')

print('1. Divisao /')
print('2. Multiplicação *')

op = str(input())
if op == '1':
    print(f'{n1} / {n2} é igual a {r1:.1f}')
elif op == '2':
    print(f'{n1} * {n2} é igual a {r2}')
else:
    print('Opção invalida!!!')