import numpy as np

'''#Crianção de Matrix
x = np.ones(2)
y = np.eye(2)
print(f'x', x)
print(f'y', y)

#soma
print(f'soma de 2 arrays: \n', x+y)
print(f'Soma com BroadCast:\n ', y + 2)

#subtração
print(f'Subtração de 2 arrays:\n ', y - 2)

##divisao
print('Divisao de 2 Arrays:\n ', y / 2)

#multiplicação
print('Multiplicão por elemento: \n', y * x)
print('Multiplicação de BroadCast: \n', y * 2)
print('Multiplicação Matricial: \n', np.dot(x, y))'''

#multiplicação entre matrizes
m1 = np.random.randint(1, 20, (2, 2))
m2 = np.random.randint(2, 30, (2, 2))
print(m1)
print('\n')
print(m2)
print('\n')
m3 = m1.dot(m2)
print(m3)

