print('Vamos descobrir de vc é maior de idade! \n')
an = int(input('qual o ano q vc nasceu...'))
ah = int(input('Em qual ano estamos...'))
idade = ah - an
if idade < 18:
    print(f'Vc possui {idade} anos, vc é menor de idade.')
else:
    print(f'Vc possui {idade} anos, vc é maior de idade.')
