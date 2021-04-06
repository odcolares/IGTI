nome = str(input('Digite seu nome...\n')).capitalize()
print(f'Olá {nome}, vc gosta do seu nome?')
resp = str(input('Escolha Sim/S ou Nao/N:\n'))
if resp in 'SIM S sim s':
    print('Vc tem amor proprio!')
elif resp in 'NAO N NÃO não nao n':
    print('Que chato!')
else:
    print('Vc é bichao!')