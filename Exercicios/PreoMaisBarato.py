p1 = float(input('valor 1: '))
p2 = float(input('valor 2: '))
p3 = float(input('valor 3: '))

if p1 > p2 > p3:
    print(f'{p3}')
elif p1 > p2:
    print(f'{p2}')
else:
    print(f'{p1}')