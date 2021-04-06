from time import sleep
print('Vamos iniciar uma contagem regressiva? ')
i = int(input('Digite o inicio da contagem: '))
f = int(input('Digite o final da contagem: '))
for z in range(i, f-1, -1):
    print(z)
    sleep(.5)
print('Fim...Boom!')