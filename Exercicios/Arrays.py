import numpy as np
#Criaçã de Arrays
'''a = np.array([[0, 1, 2], [3, 4, 5]])
print('Seu Arrays é:\n', a)
print('No de Dimensoes: ', a.ndim) #NoDeDimensoes
print('Formato do Arrays: ', a.shape) #FormatoDoArrays
print('Tamanho de linhas: ', len(a)) #TamanhoDeLinhas'''

'''l = [1, 2, 3]
x = np.array(l)
print(f'{l}')
print(f'', x.shape)

l = [1, 2], [3, 4]
x = np.array(l)
print(f'{l} com shape de', x.shape)

dim = (4, 2)
x = np.zeros(dim)
print('x: \n', x)
print('shape', x.shape)

dim = (4, 2)
x = np.ones(dim)
print('x: \n', x)
print('shape', x.shape)

#Arrays espaçados
xmin, xmax = 10, 25
x =np.linspace(start=xmin, stop=xmax, num=6)
print(f'{x} comprimento do shape é: ', x.shape)

#Matriz identidade
n = 12
x = np.eye(n)
print(f'{x}')
print(f'shape', x.shape)

b = np.arange(0, 10+1, 1) #Funcao Arange
print(b)'''

#Matriz aleatoria
e = np.random.rand(3, 2)
print('Arrays aleatorios...', e)
