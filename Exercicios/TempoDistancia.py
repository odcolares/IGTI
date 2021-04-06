dis = float(input('Qual a sua distancia em km: '))
temp = int(input('Tempo de percurso em horas: '))

vm = dis/temp

if vm > 110:
    print('Velocidade de {:.1f} KM {}ultrapassa o permitido.' .format(vm, '\033[1;31m'))
else:
    print('Velocidade {:.1f} KM esta {}dentro do permitido.' .format(vm, '\033[1;32m'))
