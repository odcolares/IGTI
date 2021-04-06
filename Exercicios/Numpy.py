import numpy as np

z = np.array([[1, 3, 7],
             [4, 11, 21],
             [42, 8, 9]])
print('x: \n', z)

print('Tranformar...\n', z.reshape(9, 1)) #ReShape
print('Transposição...\n', z.T) #transposição

print('A soma é...', np.sum(z, axis=0)) #SomaDosEixos
print('A soma é...', np.sum(z, axis=1)) #SomaDosEixos

print('Media....', np.mean(z, axis=0)) #Media

